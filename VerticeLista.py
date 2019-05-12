class VerticeLista():

    def criar(self, numVertice):
        self.num = numVertice
        self.vizinhos = []

    def incluirVizinho(self, vizinho):
        self.vizinhos.append(vizinho)