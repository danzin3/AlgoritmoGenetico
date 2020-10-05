
import populacao
if __name__ == '__main__':
    objPop = populacao.Populacao(3,10,"FitnessFunction",0,6)
    print("Indivíduos Antes da mutação:")
    objPop.showPopulacao()
    objPop.buscarMelhorIndviduo()
    objPop.showMelhoresIndividuos()

    objPop.mutacaoIndividuos()
    print("-----------------------------------------------------------------")
    print("Indivíduos Depois da Mutação")
    objPop.showPopulacao()
    objPop.buscarMelhorIndviduo()
    objPop.showMelhoresIndividuos()
    