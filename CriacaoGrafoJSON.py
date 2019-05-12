#Arquivo que, com um N determinado, cria em grafo com M aleatório(respeitando o limite máximo)
#O grafo(Ccom nome, lista de vértices e lista de arestas) é armazenado em um arquivo .json na pasta /JSON

import json
from random import randint
from Grafo import Grafo

grafoTeste = Grafo()

#n = randint(1, 9)
n = 5


vertices = []
for x in range(n):
    vertices.append(str(x+1))

print("n(vertices):" + str(n))
maxArestas = n * (n - 1) / 2
print("max arestas:" + str(maxArestas))
m = randint(0, maxArestas)
print("m(arestas):" + str(m))
arestas = []
for x in range(m):
    arestas.append(grafoTeste.geraAresta(arestas, n))

#print("arestas" + str(arestas))

nomeGrafo = 'GRAFO_ALEATORIO_GRUPO_ALAN_N_' + str(n)

arquivo = open('JSON/' + nomeGrafo + '.json', 'w')
arquivo.write('{')
arquivo.write('\n\t')
arquivo.write('"nome": "' + nomeGrafo + '",')
arquivo.write('\n\t')
arquivo.write('"vertices": ' + str(vertices).replace("'", '"') + ',')
arquivo.write('\n\t')
arquivo.write('"arestas": ' + str(arestas).replace("'", '"'))
arquivo.write('\n')
arquivo.write('}')