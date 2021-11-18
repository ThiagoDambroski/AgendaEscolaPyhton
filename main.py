from tkinter import *
from psycopg2 import *
from modelo import *
autenticado = False
user = ""
senha = ""

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
            global autenticado
            global user
            global senha
            user = fuser.get()
            senha = fsenha.get()
            autenticado = True
            login.destroy()
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
#botao
submit_btn = Button(login,text = "Entrar", command=tentar)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=50)
login.mainloop()

if(autenticado == True):

    connector = connect(
        dbname = "pyhtonProject",
        user = f"{user}",
        host = "localhost",
        password = f"{senha}"

    )

    #MASCARAS
    def format_id(event=None):

        text = fid.get()
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789": continue
            new_text += text[index]

        fid.delete(0, "end")
        fid.insert(0, new_text.title())
    def format_nome(event=None):

        text = fnome.get()
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if text[index] in "0123456789": continue
            new_text += text[index]

        fnome.delete(0, "end")
        fnome.insert(0, new_text.title())

    def format_nomeu(event=None):

        text = nome.get()
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if text[index] in "0123456789": continue
            new_text += text[index]

        nome.delete(0, "end")
        nome.insert(0, new_text.title())

    #cpf

    def format_cpf(event=None):

        text = fcpf.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789": continue
            if index in [2, 5]:
                new_text += text[index] + "."
            elif index == 8:
                new_text += text[index] + "-"
            else:
                new_text += text[index]

        fcpf.delete(0, "end")
        fcpf.insert(0, new_text)
    def format_cpfu(event=None):

        text = cpf.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789": continue
            if index in [2, 5]:
                new_text += text[index] + "."
            elif index == 8:
                new_text += text[index] + "-"
            else:
                new_text += text[index]

        cpf.delete(0, "end")
        cpf.insert(0, new_text)
    #notas
    def format_nota1(event=None):

        text = fnota1.get()[:5]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789.": continue
            new_text += text[index]


        fnota1.delete(0, "end")
        fnota1.insert(0, new_text)

    def format_nota1u(event=None):

        text = nota1.get()[:5]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789.": continue
            new_text += text[index]


        nota1.delete(0, "end")
        nota1.insert(0, new_text)

    def format_nota2(event=None):

        text = fnota2.get()[:5]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789.": continue
            new_text += text[index]

        fnota2.delete(0, "end")
        fnota2.insert(0, new_text)

    def format_nota2u(event=None):

        text = nota2.get()[:5]
        new_text = ""

        if event.keysym.lower() == "backspace": return

        for index in range(len(text)):

            if not text[index] in "0123456789.": continue
            new_text += text[index]

        nota2.delete(0, "end")
        nota2.insert(0, new_text)

    #funçoes

    def submit():
        connector = connect(
            dbname="pyhtonProject",
            user=f"{user}",
            host="localhost",
            password=f"{senha}"

        )
        cur = connector.cursor()

        notas = Notas(float(fnota1.get()),float(fnota2.get()))
        aluno = Aluno(fid.get(),fnome.get(),fcpf.get(),notas)
        #adicionando ao banco
        comando_aluno = '''INSERT INTO aluno(idaluno,nome,cpf,status) VALUES(%s,%s,%s,%s)'''
        status = f"{aluno.status()}"
        cur.execute(comando_aluno,(aluno.id,aluno.nome,aluno.cpf,status))


        comando_nota = '''INSERT INTO notas(nota1,nota2,aluno_idaluno)
        VALUES(%s,%s,%s)'''
        cur.execute(comando_nota,(notas.nota1,notas.nota2,aluno.id))
        connector.commit()
        cur.close()
        connector.close()
        fid.delete(0, END)
        fnome.delete(0, END)
        fcpf.delete(0, END)
        fnota1.delete(0, END)
        fnota2.delete(0, END)

    def show():
        connector = connect(
            dbname="pyhtonProject",
            user=f"{user}",
            host="localhost",
            password=f"{senha}"

        )
        show = Tk()
        show.title('Update')
        show.geometry("400x400")

        cur = connector.cursor()

        cur.execute("Select * FROM aluno a,notas n WHERE a.idaluno = n.aluno_idaluno ORDER BY idaluno ASC")
        tabelas = cur.fetchall()
        print_tabelas = 'ID | NOME | CPF | NOTA 1 | NOTA 2 | MEDIA | STATUS \n' + ("-" * 57) + "\n"
        final = ''
        for c in tabelas:
            count = 0
            media = 0
            for i in c:
                if count == 3:
                    final = f"{i}  "
                elif count == 4:
                    print_tabelas += ''
                elif count == 5:
                    print_tabelas += f"{i} | "
                    media += int(i)
                elif count == 6:
                    print_tabelas += f"{i} | "
                    media += int(i)
                    media /= 2
                elif count == 7:
                    print_tabelas += ''
                else:
                    print_tabelas += f"{i} | "
                count += 1
            print_tabelas += f"{media} | "
            print_tabelas += final
            print_tabelas += f"\n"

        show_label = Label(show,text=print_tabelas)
        show_label.grid(row = 0,column=0,columnspan=2 )

        connector.commit()
        cur.close()
        connector.close()
        show.mainloop()

    def delete():
        connector = connect(
            dbname="pyhtonProject",
            user=f"{user}",
            host="localhost",
            password=f"{senha}"

        )
        cur = connector.cursor()
        comando_deletar_nota = f"DELETE from notas WHERE aluno_idaluno = {delete_box.get()} "
        cur.execute(comando_deletar_nota)
        comando_deletar_aluno = f"DELETE from aluno WHERE idaluno = {delete_box.get()} "
        cur.execute(comando_deletar_aluno)

        delete_box.delete(0, END)
        connector.commit()
        cur.close()
        connector.close()

    def save():
        connector = connect(
            dbname="pyhtonProject",
            user=f"{user}",
            host="localhost",
            password=f"{senha}"

        )
        cur = connector.cursor()
        notas = Notas(float(nota1.get()), float(nota2.get()))
        aluno = Aluno(id_clonado, nome.get(), cpf.get(), notas)

        # adicionando ao banco
        comando_aluno = f'''UPDATE aluno SET(nome,cpf,status) = (%s,%s,%s) WHERE idaluno = {id_clonado} '''
        status = f"{aluno.status()}"
        cur.execute(comando_aluno, (aluno.nome, aluno.cpf, status))

        comando_nota = f'''UPDATE notas SET (nota1,nota2) = (%s,%s)WHERE 
                    aluno_idaluno = {id_clonado}'''
        cur.execute(comando_nota, (notas.nota1, notas.nota2))
        connector.commit()
        cur.close()
        connector.close()
        updatef.destroy()
    def update():
        # global
        global id_clonado
        global nome
        global cpf
        global nota1
        global nota2
        global updatef
        #
        updatef = Tk()
        updatef.title('Update')
        updatef.geometry("350x200")
        id_clonado = update_box.get()
        #ajustanfdo tablea
        connector = connect(
            dbname="pyhtonProject",
            user=f"{user}",
            host="localhost",
            password=f"{senha}"

        )
        cur = connector.cursor()

        cur.execute(f"Select * FROM aluno a,notas n WHERE a.idaluno = {id_clonado} AND aluno_idaluno = {id_clonado}")
        tabelas = cur.fetchall()
        # Nome aluno
        nome_label = Label(updatef, text="Nome aluno")
        nome_label.grid(row=1, column=0)
        nome = Entry(updatef, width=30)
        nome.bind("<KeyRelease>", format_nomeu)
        nome.grid(row=1, column=1, padx=20)
        # Cpf aluno
        cpf_label = Label(updatef, text="cpf aluno")
        cpf_label.grid(row=2, column=0)
        cpf = Entry(updatef, width=30)
        cpf.bind("<KeyRelease>", format_cpfu)
        cpf.grid(row=2, column=1, padx=20)
        # Nota1
        nota1_label = Label(updatef, text="primeira nota")
        nota1_label.grid(row=3, column=0)
        nota1 = Entry(updatef, width=30)
        nota1.bind("<KeyRelease>", format_nota1u)
        nota1.grid(row=3, column=1, padx=20)
        # Nota2
        nota2_label = Label(updatef, text="segunda nota")
        nota2_label.grid(row=4, column=0)
        nota2 = Entry(updatef, width=30)
        nota2.bind("<KeyRelease>", format_nota2u)
        nota2.grid(row=4, column=1, padx=20)
        for c in tabelas:
               nome.insert(0, c[1])
               cpf.insert(0, c[2])
               nota1.insert(0, c[5])
               nota2.insert(0, c[6])

        save_btn = Button(updatef, text="Salvar", command=save)
        save_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        cur.close()
        connector.close()
        update_box.delete(0, END)

    root = Tk()
    root.title('Projeto pyhton')
    root.geometry("400x400")

    # Id aluno
    id_label = Label(root, text = "ID aluno")
    id_label.grid(row=0, column=0)
    fid = Entry(root, width = 30)
    fid.bind("<KeyRelease>", format_id)
    fid.grid(row = 0, column = 1, padx =20)
    # Nome aluno
    nome_label = Label(root, text = "Nome aluno")
    nome_label.grid(row=1, column=0)
    fnome = Entry(root, width = 30)
    fnome.bind("<KeyRelease>", format_nome)
    fnome.grid(row = 1, column = 1, padx =20)
    # Cpf aluno
    cpf_label = Label(root, text = "cpf aluno")
    cpf_label.grid(row=2, column=0)
    fcpf = Entry(root, width = 30)
    fcpf.bind("<KeyRelease>", format_cpf)
    fcpf.grid(row = 2, column = 1, padx =20)
    # Nota1
    nota1_label = Label(root, text = "primeira nota")
    nota1_label.grid(row=3, column=0)
    fnota1 = Entry(root, width = 30)
    fnota1.bind("<KeyRelease>", format_nota1)
    fnota1.grid(row = 3, column = 1, padx =20)
    # Nota2
    nota2_label = Label(root, text = "segunda nota")
    nota2_label.grid(row=4, column=0)
    fnota2 = Entry(root, width = 30)
    fnota2.bind("<KeyRelease>", format_nota2)
    fnota2.grid(row = 4, column = 1, padx =20)

    # adicionar ao banco
    submit_btn = Button(root,text = "Adicionar ao banco de dados", command=submit)
    submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #Show
    show_btn = Button(root,text="Mostra dados",command= show)
    show_btn.grid(row = 7,column=0,columnspan=2,pady=10,padx=10,ipadx=140)



    #deletar
    delete_box = Entry(root,width=30)
    delete_box.grid(row = 10,column=1)
    delete_label = Label(root, text = "Excluir ID aluno")
    delete_label.grid(row=10,column=0)
    delete_btn = Button(root,text="Deletar dados",command= delete)
    delete_btn.grid(row = 9,column=0,columnspan=2,pady=10,padx=10,ipadx=140)

    #Update
    update_box = Entry(root,width=30)
    update_box.grid(row = 12,column=1)
    update_label = Label(root, text = "Update ID aluno")
    update_label.grid(row=12,column=0)
    update_btn = Button(root,text="Update dados",command= update)
    update_btn.grid(row = 11,column=0,columnspan=2,pady=10,padx=10,ipadx=140)

    connector.close()
    root.mainloop()