class Aluno:
    def __init__(self):
        self.listasAlunos = [["Davi", "xxxxxxx@xxx", 3, "SI", "15464-654"],
                             ['Lucas', 'zzzzz@zzz', 5, 'ADM', '56465-546'],
                             ['Renata', 'yyyyyyyy@yyy', 7, 'LETRAS', '.65498-321']]
        self.matricula = 10

    def cadastrarAluno(self):
        nome= input("\nPor favor Preencha os campos abaixo:"
                    "\nNome do Aluno:")
        email= input("E-mail:")
        self.matricula +=1
        matricula = self.matricula
        cep = input("Cep(ex.:00000-000):")
        curso= input("Insira o Curso:").upper()
        aluno= [nome,email,matricula,curso,cep]
        self.listasAlunos.append(aluno)
        return
    def listarAlunos(self):
        for aluno in self.listasAlunos:
            print(aluno,"\n")
        return
    def buscarAluno(self):
        buscarMatricula= int(input("\nInsira a matricula do aluno:"))
        for aluno in self.listasAlunos:
            n, e, m, cur, c = aluno
            if m == buscarMatricula:
                print(aluno,"\n")
        return

