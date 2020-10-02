from random import randint
import individuo

if __name__ == '__main__':
    objInd1 = individuo.Individuo(10,randint,"(x^2)-(5x)+6",0,6)
    #objInd2 = individuo.Individuo(10,randint,"(x^2)-(5x)+6",0,6)

    objInd1.pressaoAmbiente()
    #objInd2.recebeDados(objInd1)

    print("Dados Do Indivíduo 1 antes da mutação:")
    objInd1.imprimirIndividuo()

    objInd1.mutacao()
    objInd1.pressaoAmbiente()

    print("---------------------------------------------------------------------")
    print("Dados Do Indivíduo 1 depois da mutação:")
    objInd1.imprimirIndividuo()
    