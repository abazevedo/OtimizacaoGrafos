from random import randint

class Grafo():

    def arestaExiste(self, novaAresta, vetorArestas):
        for aresta in vetorArestas:
            if aresta == novaAresta:
                return 1
            else:
                if (aresta[0] == novaAresta[1]) and (aresta[1] == novaAresta[0]):
                    return 1
        return 0

    def geraAresta(self, vetorArestas, n):
        aresta = []
        x = randint(1, n)
        aresta.append(str(x))
        y = x
        while True:
            y = str(randint(1,n))
            if y != x:
                break

        aresta.append(y)

        while True:
            if (self.arestaExiste(aresta, vetorArestas) == 0) and (aresta[0] != aresta[1]):
                return aresta
            aresta.clear()
            aresta.append(str(randint(1, n)))
            aresta.append(str(randint(1, n)))
