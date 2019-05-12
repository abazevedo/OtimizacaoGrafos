#Dado N, é realizada leitura no arquivo .json correspondente.
#Daí, cria-se um objeto Grafo em representação de matriz.
#Em seguida, são testados os métodos de inclusão/remoção de vertice/aresta e exibição de vizinhos de um vértice e mostrados os resultados

import json
from GrafoMatriz import GrafoMatriz


n = 5

arquivo = open('JSON/GRAFO_ALEATORIO_GRUPO_ALAN_N_'+ str(n) +'.json').read()

conteudoJSON = json.loads(arquivo)
print(conteudoJSON)

GrafoExemplo = GrafoMatriz()
GrafoExemplo.criar(conteudoJSON)

print("*MATRIZ:")
for linha in GrafoExemplo.matriz:
    print(linha)
print("vertices:")
print(GrafoExemplo.n)
print("arestas:")
print(GrafoExemplo.m)
print("vizinhos do " + str(n-1) + ":")
print(GrafoExemplo.getVizinhosVertice(4))
print("----")

print("adicionar vertice")
GrafoExemplo.adicionarVertice()
print("matriz:")
for linha in GrafoExemplo.matriz:
    print(linha)
print("vertices:")
print(GrafoExemplo.n)
print("arestas:")
print(GrafoExemplo.m)
print("vizinhos do " + str(n-1) + ":")
print(GrafoExemplo.getVizinhosVertice(4))
print("----")

print("adicionar aresta")
GrafoExemplo.adicionarAresta(4,5)
print("matriz:")
for linha in GrafoExemplo.matriz:
    print(linha)
print("vertices:")
print(GrafoExemplo.n)
print("arestas:")
print(GrafoExemplo.m)
print("vizinhos do " + str(n-1) + ":")
print(GrafoExemplo.getVizinhosVertice(4))
print("----")

print("remover aresta")
GrafoExemplo.removerAresta(4,5)
print("matriz:")
for linha in GrafoExemplo.matriz:
    print(linha)
print("vertices:")
print(GrafoExemplo.n)
print("arestas:")
print(GrafoExemplo.m)
print("vizinhos do " + str(n-1) + ":")
print(GrafoExemplo.getVizinhosVertice(4))
print("----")

print("remover vertice")
GrafoExemplo.removerVertice(5)
print("matriz:")
for linha in GrafoExemplo.matriz:
    print(linha)
print("vertices:")
print(GrafoExemplo.n)
print("arestas:")
print(GrafoExemplo.m)
print("vizinhos do " + str(n-1) + ":")
print(GrafoExemplo.getVizinhosVertice(4))
print("----")




