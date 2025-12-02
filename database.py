from database import SessionLocal, Base, engine
from models.curso import Curso
from models.usuario import Usuario
from datetime import datetime

# Criar tabelas caso não existam #
Base.metadata.create_all(bind=engine)

# Criar sessão
db = SessionLocal()

# Inserir CURSOS #
cursos = [
    Curso(nome="Engenharia de Software", codigo="ESW01"),
    Curso(nome="Análise e Desenvolvimento de Sistemas", codigo="ADS02"),
    Curso(nome="Ciência da Computação", codigo="CC03"),
    Curso(nome="Sistemas de Informação", codigo="SI04"),
    Curso(nome="Redes de Computadores", codigo="RDC05"),
]

db.add_all(cursos)
db.commit()

# Inserir USUÁRIOS #
usuarios = [
    Usuario(
        nome="Ana Costa",
        email="ana.costa@email.com",
        senha_hash="123abc",
        papel="ALUNO",
        curso_id=1,
        semestre=3,
        criado_em=datetime(2025, 2, 1, 14, 20),
        ativo=True
    ),
    Usuario(
        nome="Ricardo Silva",
        email="ricardo.silva@email.com",
        senha_hash="abc321",
        papel="PROFESSOR",
        curso_id=2,
        semestre=1,
        criado_em=datetime(2025, 3, 12, 10, 11),
        ativo=True
    ),
    Usuario(
        nome="Mariana Oliveira",
        email="mariana.oli@email.com",
        senha_hash="senha123",
        papel="ALUNO",
        curso_id=1,
        semestre=5,
        criado_em=datetime(2025, 1, 5, 9, 0),
        ativo=True
    ),
    Usuario(
        nome="João Pereira",
        email="jpereira@email.com",
        senha_hash="xpto987",
        papel="ALUNO",
        curso_id=4,
        semestre=2,
        criado_em=datetime(2025, 2, 20, 8, 0),
        ativo=False
    ),
    Usuario(
        nome="Sabrina Martins",
        email="sabrina.martins@email.com",
        senha_hash="teste001",
        papel="ALUNO",,
        curso_id=3,
        semestre=4,
        criado_em=datetime(2025, 12, 14, 16, 45),
        ativo=True
    ),
]

db.add_all(usuarios)
db.commit()

# Encerrar sessão #
db.close()

print("Banco populado com sucesso!")

