
import individuo

class Populacao(object):
    """description of class"""

    # individuos   --> Lista de Indivíduos
    # nPop         --> tamanho da população
    # nInd         --> tamanho do cromossomo de cada Indivíduo
    # fitness      --> Função Fitness
    # min          --> Intervalo Mínimo real da fitness
    # max          --> Intervalo Máximo real da fitness
    # melhoresInd  --> Lista de indivíduos mais adaptáveis de cada geração
    
    melhorTodos = {}
    
    def __init__(self, tamPop, tamInd, fitnessParam, minParam, maxParam):
        self.individuos = []
        self.melhoresInd = []
        self.nPop = tamPop
        self.nInd = tamInd
        self.fitness = fitnessParam
        self.min = minParam
        self.max = maxParam
        for i in range(self.nPop):
            self.individuos.append(individuo.Individuo(self.nInd,self.fitness,self.min,self.max))
            self.individuos[i].pressaoAmbiente()

    def showPopulacao(self):
        i = 1
        for ind in self.individuos:
            print("Indivíduo ",i," :");i=i+1
            ind.showIndividuo()

    # Visto que o intuito é minimizar (por enquanto) tem de se escolher o 
    # indivíduo que possúi menor adaptabilidade
    def buscarMelhorIndviduo(self):
        self.melhoresInd.append(individuo.Individuo(self.nInd,self.fitness,self.min,self.max))
        self.melhoresInd[-1].recebeDados(self.individuos[0])
        for ind in self.individuos:
            if(ind.adaptabilidade < self.melhoresInd[-1].adaptabilidade):
                self.melhoresInd[-1].recebeDados(ind)
        

    def mutacaoIndividuos(self):
        for ind in self.individuos:
            ind.mutacao()       

    def showMelhoresIndividuos(self):
        i = 1
        for ind in self.melhoresInd:
            print("Melhor Indivíduo da: ",i," Geração:");i=i+1
            ind.showIndividuo()

    def buscarMelhorTotal(self):
        self.melhorTodos = self.melhoresInd[0]
        for ind in self.melhoresInd:
            if(ind.adaptabilidade < self.melhorTodos.adaptabilidade):
                self.melhorTodos.recebeDados(ind)
        print("Melhor de Todos: ")
        self.melhorTodos.showIndividuo()
