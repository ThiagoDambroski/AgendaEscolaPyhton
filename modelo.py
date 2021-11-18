
class Aluno:
    def __init__(self,id,nome,cpf,notas):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.notas = notas

    def media(self):
        sum = (self.notas.nota1+ self.notas.nota2) / 2
        return float(sum)

    def status(self):
        if self.media() > 7:
            return "Aprovado"
        elif self.media() >= 4 and self.media() < 7:
            return "Recuperação"
        elif self.media() < 4:
            return "Reprovado"



class Notas:
    def __init__(self,nota1,nota2):
        self.nota1 = nota1
        self.nota2 = nota2
