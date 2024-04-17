class Disciplina:
    def __init__(self):
        self.listasDis = ['Programação', 'Cálculo', 'Literatura', ]
    def listDisci(self):
        for i in self.listasDis:
            print(i)
        return