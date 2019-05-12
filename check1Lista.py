#Dado N, é realizada leitura no arquivo .json correspondente.
#Daí, cria-se um objeto Grafo em representação de lista.
#Em seguida, são testados os métodos de inclusão/remoção de vertice/aresta e exibição de vizinhos de um vértice e mostrados os resultados

import json
from GrafoLista import GrafoLista

n = 5

arquivo = open('JSON/GRAFO_ALEATORIO_GRUPO_ALAN_N_'+ str(n) +'.json').read()

conteudoJSON = json.loads(arquivo)
print(conteudoJSON)

GrafoExemplo = GrafoLista()
GrafoExemplo.criar(conteudoJSON)

print("*LISTA:")

print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")

print("adicionar vertice")
GrafoExemplo.adicionarVertice()
print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")

print("adicionar aresta")
GrafoExemplo.adicionarAresta(1,3)
print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")

print("remover aresta [1,2]")
GrafoExemplo.removerAresta(1,2)
print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")

print("remover vertice 4")
GrafoExemplo.removerVertice(4)
print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")

print("remover vertice 6")
GrafoExemplo.removerVertice(6)
print("n(vertices): " + str(GrafoExemplo.n))
print("m(arestas): " + str(GrafoExemplo.m))
print("vertices:")
for x in range(GrafoExemplo.n):
    print(GrafoExemplo.vertices[x].num)
print("vizinhos de cada:")
for x in range(1, GrafoExemplo.n + 1):
    print(GrafoExemplo.getVizinhosVertice(x))
print("----")