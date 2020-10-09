
import populacao
if __name__ == '__main__':
    objPop = populacao.Populacao(3,10,"FitnessFunction",0,6)
    print("Digite a quantidade de gerações:")
    quant = input()
    for i in range(int(quant)):
        objPop.showPopulacao()
        objPop.buscarMelhorIndviduo()
        objPop.mutacaoIndividuos()

    objPop.showMelhoresIndividuos()
    objPop.buscarMelhorTotal()

    