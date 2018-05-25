import itertools

class CombinationGenerator(object):
    #Construtor de classe, pode receber comb(3) ou comb(5,3) por exemplo
    def __init__(self, combinationLength, subSetSize = None): #Construtor da classe.
        self.combinationLength = combinationLength
        self.subSetSize = subSetSize
        self.binaryList = comb(combinationLength, subSetSize)

    #metodo de classe que retorna o indice da combinação passada por parametro
    def getCombAtIndex(self, index):
        subsetList = self.binaryList[0]
        if (index >= len(subsetList)):
            print('{}{}{}{}'.format(subsetList, ' at(', index, ') == Indice maior que o tamanho do vetor informado'))
            return
        if subsetList[index] == 1:
            print('{}{}{}{}'.format(subsetList, ' at(', index, ') == TRUE'))
        else:
            print('{}{}{}{}'.format(subsetList, ' at(', index, ') == FALSE'))

#sobrecarga de metodo, para comb se pode passar apenas um parametro ou dois
def comb(combinationLength, subsetsize = None):
    #Para montar as combinações utilizo a biblioteca nativa em python itertools:
    # Ela possui metodos para trabalhar com produto cartesiano, combinações e permutações

    binaryList = list(itertools.product([0, 1], repeat=combinationLength))
    combinationWithSubSet = []

    for i in binaryList:
        if subsetsize is None:
            # codigo para imprimir cada combinação em uma linha diferente
            print(", ".join([str(l).rjust(3) for l in i]))
        else:
            # Para a combinação de numero binario com 5 digitos 3 a 3,
            # somente são aceitos as series cuja somatorios seja igual a 3,
            # ou seja, para todas estas combinação a soma de seus elementos é sempre 3
            if(sum(i) == subsetsize):
                # codigo para imprimir cada combinação em uma linha diferente
                lineOutput = ", ".join([str(l).rjust(3) for l in i])
                combinationWithSubSet.append(i)
                print(lineOutput)
    if subsetsize is None:
        return binaryList
    return combinationWithSubSet

#Função main para poder testar os metodos desta classe
if __name__ == '__main__':

    print("Testa o primeiro exemplo comb(3):")

    # Cria a combinação, exemplo 1(se passa apenas um parametro)
    combinationGenerator1 = CombinationGenerator(3)

    print("Testa o segundo exemplo comb(5,3):")

    #Cria a combinação, exemplo 2(se passa dois parametros para o construtor)
    combinationGenerator2 = CombinationGenerator(5,3)
    combinationGenerator2.getCombAtIndex(0)
    combinationGenerator2.getCombAtIndex(3)
