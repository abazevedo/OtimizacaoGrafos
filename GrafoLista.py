from VerticeLista import VerticeLista

class GrafoLista():

    def getIndicePorValor(self, lista, num):

        for idx, val in enumerate(lista):
            if val.num == num:
                return idx

    def estaNaLista(self, lista, elemento):
        for item in lista:
            if item == elemento:
                return 1
        return 0

    def criarLista(self, arestas):
        for aresta in arestas:

            #verificar se B está na lista dos vizinhos de A
            indiceLista = self.getIndicePorValor(self.vertices, aresta[0])
            if self.estaNaLista(self.vertices[indiceLista].vizinhos, aresta[1]) == 0:
                self.vertices[indiceLista].incluirVizinho(aresta[1])

            # verificar se A está na lista dos vizinhos de B
            indiceLista = self.getIndicePorValor(self.vertices, aresta[1])
            if self.estaNaLista(self.vertices[indiceLista].vizinhos, aresta[0]) == 0:
                self.vertices[indiceLista].incluirVizinho(aresta[0])

    def criar(self, conteudo):
        self.nome = conteudo["nome"]
        self.n = len(conteudo["vertices"])
        self.m = len(conteudo["arestas"])
        self.vertices = []
        for v in conteudo["vertices"]:
            vertice = VerticeLista()
            vertice.criar(v)
            self.vertices.append(vertice)

        self.criarLista(conteudo["arestas"])

    def getVizinhosVertice(self ,vertice):
        return self.vertices[vertice-1].vizinhos

    def adicionarVertice(self):
        vertice = VerticeLista()
        vertice.criar(str(self.n+1))
        self.vertices.append(vertice)
        self.n += 1

    def removerArestasDeVertice(self, numVertice):
        for vertice in self.vertices:
            for idx,val in enumerate(vertice.vizinhos):
                if val == str(numVertice):
                    vertice.vizinhos.pop(idx)
                    self.m -= 1

    def removerVertice(self, numVertice):
        indiceLista = self.getIndicePorValor(self.vertices, str(numVertice))
        self.vertices.pop(indiceLista)
        self.n -= 1
        self.removerArestasDeVertice(numVertice)

    def adicionarAresta(self, v1, v2):
        indiceLista = self.getIndicePorValor(self.vertices, str(v1))
        if self.estaNaLista(self.vertices[indiceLista].vizinhos, str(v2)) == 0:
            self.vertices[indiceLista].incluirVizinho(str(v2))
        else:
            return

        indiceLista = self.getIndicePorValor(self.vertices, str(v2))
        if self.estaNaLista(self.vertices[indiceLista].vizinhos, str(v1)) == 0:
            self.vertices[indiceLista].incluirVizinho(str(v1))
        self.m +=1

    def removerAresta(self, v1, v2):
        indiceLista = self.getIndicePorValor(self.vertices, str(v1))
        for idx, val in enumerate(self.vertices[indiceLista].vizinhos):
            if val == str(v2):
                self.vertices[indiceLista].vizinhos.pop(idx)

        indiceLista = self.getIndicePorValor(self.vertices, str(v2))
        for idx, val in enumerate(self.vertices[indiceLista].vizinhos):
            if val == str(v1):
                self.vertices[indiceLista].vizinhos.pop(idx)
        self.m -= 1
