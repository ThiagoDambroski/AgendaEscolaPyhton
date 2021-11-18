from psycopg2 import *
x = str(input("USER: "))
Y = str(input("SENHA: "))

connector = connect(
    dbname = "pyhtonProject",
    user = f"{x}",
    host = "localhost",
    password = f"{y}"

)

cur = connector.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS aluno (
  idaluno INT NOT NULL UNIQUE PRIMARY KEY,
  nome VARCHAR(45) NOT NULL,
  cpf VARCHAR(14) NOT NULL UNIQUE,
  status VARCHAR(14) NOT NULL);''')
cur.execute('''CREATE TABLE IF NOT EXISTS notas (
  idnotas SERIAL NOT NULL PRIMARY KEY,
  nota1 FLOAT NULL,
  nota2 FLOAT NULL,
  aluno_idaluno INT NOT NULL,
    FOREIGN KEY (aluno_idaluno)
    REFERENCES aluno (idaluno));''')


connector.commit()

cur.close()
connector.close()
