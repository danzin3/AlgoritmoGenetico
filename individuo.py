
from random import randint
class Individuo:
    """Classe responsável por determinar atributos e operações no Indivíduo"""
    # n              --> Tamanho máximo do cromossomo
    # cromossomo     --> Vetor de bits para representar o cromossomo
    # fenotipo       --> Valor representativo do cromossomo em decimal
    # fenNormalizado --> Valor do Fenótipo normalizado
    # adaptabilidade --> Adapatabilidade do indivíduo
    # funcaoFitness  --> String para armazenar a função que representa o ambiente
    # numAleatorio   --> Objeto para geração de número aleatórios
    # intervalMin    --> Menor valor de x (raiz) na função fitness
    # intervalMax    --> Maior valor de x (raiz) da função fitness

    numAleatorio = {}

    def __init__(self,tam,ambiente,minVal,maxVal):
        # Atributos internos do Indivíduo:
        self.fenotipo = 0
        self.fenNormalizado = 0
        self.adaptabilidade = 0
        self.cromossomo = []
        self.numAleatorio = randint
        # Atributos Vindos Do Parâmetro de Construção:
        for i in range(tam):
            self.cromossomo.append(self.numAleatorio(0,1))
        self.n = tam
        self.funcaoFitness = ambiente
        self.intervalMin = minVal
        self.intervalMax = maxVal


    def gerarFenotipo(self):
        i=self.n-1;
        for bit in self.cromossomo:
            self.fenotipo = self.fenotipo + (bit * pow(2,i));i=i-1
        #print("Fenótipo: ",self.fenotipo)


    def normalizarFenotipo(self):
        self.fenNormalizado = (self.intervalMin + (self.intervalMax - self.intervalMin)) * (self.fenotipo/(pow(2,self.n) - 1))
        #print("fen Normalizado: ",self.fenNormalizado)

    def gerarAdaptabilidade(self):
        # Vou usar uma função fixa para testar, depois usar a string funcaoFitness
        self.adaptabilidade = (pow(self.fenNormalizado,2) - (5*self.fenNormalizado) + 6)
        #print("Adaptabilidade: ",self.adaptabilidade)

    # Método que simula a pressão do Ambiente no Indivíduo
    def pressaoAmbiente(self):
        self.gerarFenotipo(); # Obtem o valor decimal do vetor de bits(cromossomo)
        self.normalizarFenotipo();
        self.gerarAdaptabilidade(); # Obtem a adaptabilidade com o fenótipo já normalizado

    # Método que recebe um indivíduo como parâmetro e obter os dados desse indivíduo
    # Pode-se entender que esse método realiza uma cópia do Indivíduo passado como parametro
    def recebeDados(self,IndParam):
        # A cópia só poderá ser feita se o tamano do cromossomo dos Indivíduos forem Iguais
        if(self.n == IndParam.n):
            self.fenotipo = IndParam.fenotipo
            self.fenNormalizado = IndParam.fenNormalizado
            self.adaptabilidade = IndParam.adaptabilidade
            self.cromossomo = IndParam.cromossomo.copy()
            self.n = IndParam.n
            self.funcaoFitness = IndParam.funcaoFitness
            self.numAleatorio = IndParam.numAleatorio
            self.intervalMin = IndParam.intervalMin
            self.intervalMax = IndParam.intervalMax
        else:
            print("Não é possível clonar Individuos com o tamanho do cromossomo difentes")


    def showIndividuo(self):
        print("Cromossomo: ",self.cromossomo)
        print("Tamanho: ",self.n)
        print("fenótipo: ",self.fenotipo)
        print("fenótipo Normalizado: ",self.fenNormalizado)
        print("Adaptabilidade: ",self.adaptabilidade)
        print("Fitness: ",self.funcaoFitness)
        print("xMin: ",self.intervalMin)
        print("xMax: ",self.intervalMax)
        print("--------------------------------------------------------------")

    def mutacao(self):
        aux = self.numAleatorio(0,(self.n -1))
        if(self.cromossomo[aux] == 1):
            self.cromossomo[aux] = 0
        else:
            self.cromossomo[aux] = 1
        self.pressaoAmbiente()
        