class Curso:
    def __init__(self):
        self.cursos = ['SI', 'ADM', 'LETRAS']
    def listCursos(self):
        for i in self.cursos:
            print(i)
        return