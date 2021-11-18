from tkinter import *
from psycopg2 import *
from modelo import *
autenticado = False
def tentar():
      try:
            connector = connect(
                  dbname="pyhtonProject",
                  user= f"{fuser.get()}",
                  host="localhost",
                  password=f"{fsenha.get()}"

            )
            cur = connector.cursor()
            cur.close()
            connector.close()
            login.destroy()
            global autenticado
            autenticado = True
      except:
            erro = Tk()
            erro.title('Erro')
            erro.geometry("230x50")
            text = Text(erro)
            text.insert(INSERT,"Informaçoes invalidas")
            text.pack()
            erro.mainloop()
            fuser.delete(0, END)
            fsenha.delete(0, END)

login = Tk()
login.title('Projeto pyhton')
login.geometry("300x110")
# user
user_label = Label(login, text = "Usuario")
user_label.grid(row=0, column=0)
fuser = Entry(login, width = 30)
fuser.grid(row = 0, column = 1, padx =20)
# senha
senha_label = Label(login, text = "Senha")
senha_label.grid(row=1, column=0)
fsenha = Entry(login, width = 30,show = "*")
fsenha.grid(row = 1, column = 1, padx =20)

###
submit_btn = Button(login,text = "Entrar", command=tentar)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)
login.mainloop()
if(autenticado == True):
      print("okay")
#postgres


# print("digite os dados do aluno")
# id = int(input("ID:"))
# nome_aluno = str(input("Nome: "))
# cpf = str(input("CPF: "))
# materia = str(input("Nome da materia: "))
# nota1 = float(input("primeira nota: "))
# nota2 = float(input("segunda nota: "))
#
# notas = Notas(nota1,nota2)
# aluno = Aluno(1,nome_aluno,cpf,notas)

# comando_aluno = '''INSERT INTO aluno(idaluno,nome,cpf,status) VALUES (:id,:nome,:cpf,:status)'''
# cur.execute(comando3,{"id": aluno.id,
#                      "nome": aluno.nome,
#                       "cpf": aluno.cpf,
#                        "staus": aluno.status()})

#comando_nota = '''INSERT INTO notas(nota1,nota2,aluno_idaluno,materia_idmateria)
#VALUES (:nota1,:nota2,:idaluno,:idmateria)'''
# cur.execute(comando3,{"nota1": notas.nota1,
#                      "nota2": notas.nota2,
#                       "idaluno": aluno.id,
#                        "idmateria": materia.id})

#comando_materia = '''INSERT INTO materia(nome) VALUES (:nome)'''
# cur.execute(comando3,{"nome": materia.nome})

#
# print(f"Nome: {aluno.nome} | primeira nota: "
#       f"{aluno.notas.nota1}| segunda nota {aluno.notas.nota2} | Media {aluno.media()} "
#       f"| Status: {aluno.status()} ")

# comando_aluno = '''INSERT INTO aluno(idaluno,nome,cpf,status) VALUES(%s,%s,%s,%s)'''
#     status = aluno.status()
#     cur.execute(comando_aluno,(aluno.id,aluno.nome,aluno.cpf,status))
#
# comando_aluno = '''INSERT INTO aluno(idaluno,nome,cpf,status) VALUES(:id,:nome,:cpf,:status)'''
#     cur.execute(comando_aluno,{"id": aluno.id,
#                          "nome": aluno.nome,
#                           "cpf": aluno.cpf,
#                            "staus": aluno.status()})