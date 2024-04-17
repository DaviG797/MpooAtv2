from sala import Sala
from aluno import Aluno
from professor import Professor
from curso import Curso
from disciplina import Disciplina

class Menu :

    def __init__(self):
        self.value=0
    def exibirMenu(self):
        aluno = Aluno()
        prof= Professor()
        curso= Curso()
        disci=Disciplina()
        sala= Sala()
        while True:
            option = int(input("*** Bem vindo ao casdatro do Aluno da Uast *** "
                           "\n1- Cadastar Aluno"
                           "\n2-Listar Alunos"
                           "\n3-Buscar Aluno"
                           "\n4-Professores"
                           "\n5-Cursos"
                           "\n6-Disciplinas"
                           "\n7-Salas"
                           "\n0-Sair"
                           "\nEscolha uma opção:"))
            if option == 1:
                aluno.cadastrarAluno()
            elif option == 2:
                aluno.listarAlunos()
            elif option == 3:
                aluno.buscarAluno()
            elif option == 4:
                prof.professor()
            elif option == 5:
                curso.listCursos()
            elif option == 6:
                disci.listDisci()
            elif option == 7:
                sala.listSala()
            elif option == 0:
                break
            else:
                print("\n***Opção não disponivel!***\n")


adm=Menu()
adm.exibirMenu()