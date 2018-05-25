# Construtor de classe
class PartitionGenerator(object):
    def __init__(self, cardinality): #Construtor da classe.
        self.cardinality = cardinality
        self.list = partition(cardinality)

    # metodo de classe para obter algum elemento da lista de combinações
    def getPartition(self, index):
        # visualmente imprimimos o vetor começando de 1, por isso adicionamos 1 ao indice passado por parametro
        print('{}{} = {}'.format("getPartition at ", index+1, self.list[index]))



def partition(cardinality):
    lista = []
    # vetor inicial dado a cardinalidade
    # ex: Se cardinalidade = 4 ; vetor = [0,1,2,3]
    rawVector = list(range(0, cardinality))
    for n, p in enumerate(partitionRecursion(rawVector), 1):
        print(n, sorted(p))
        lista.append(sorted(p))
    return lista


# função recursiva que vai montando as combinações
def partitionRecursion(collection):
    #caso base, o tamanho do vetor é 1
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partitionRecursion(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset
        yield [ [ first ] ] + smaller

# função main para poder testar os metodos desta classe
if __name__ == '__main__':
     #partition(4)
     cardinality = 4
     #Cria uma partição com cardinalidade 4
     partitionRecursion = PartitionGenerator(cardinality)
    
     partitionIndex = 2
     #Testa o metodo que busca algum elemento da lista.
     partitionRecursion.getPartition(partitionIndex)
