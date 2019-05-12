class GrafoMatriz():

    def criarMatriz(self, arestas):
        for x in range(self.n):
            vetor = []
            for y in range(self.n):
                vetor.append(0)

            self.matriz.append(vetor)

        for par in arestas:
            self.matriz[int(par[0])- 1][int(par[1])- 1] = 1
            self.matriz[int(par[1])- 1][int(par[0])- 1] = 1

        return self.matriz

    def criar(self, conteudo):
        self.nome = conteudo["nome"]
        self.n = len(conteudo["vertices"])
        self.m = len(conteudo["arestas"])
        self.matriz = []
        self.matriz = self.criarMatriz(conteudo["arestas"])

    def getVizinhosVertice(self ,vertice):
        vizinhos = []
        for idx, val in enumerate(self.matriz[vertice-1]):
            if val == 1:
                vizinhos.append(idx+1)

        return vizinhos

    def adicionarArestasDeVertice(self):
        vetor = []
        for n in range(self.n):
            vetor.append(0)
            self.matriz[n].append(0)
        vetor.append(0)
        self.matriz.append(vetor)

    def adicionarVertice(self):
        self.adicionarArestasDeVertice()
        self.n += 1

    def removerArestasDeVertice(self, vertice):
        self.matriz.pop(vertice-1)
        for n in range(self.n - 1):
            if self.matriz[n-1][vertice-1] == 1:
                self.m -= 1
            self.matriz[n-1].pop(vertice-1)

    def removerVertice(self, vertice):
        self.removerArestasDeVertice(vertice)
        self.n -= 1

    def adicionarAresta(self, v1, v2):
        self.matriz[v1 - 1][v2 - 1] = 1
        self.matriz[v2 - 1][v1 - 1] = 1
        self.m += 1

    def removerAresta(self, v1, v2):
        self.matriz[v1 - 1][v2 - 1] = 0
        self.matriz[v2 - 1][v1 - 1] = 0
        self.m -= 1