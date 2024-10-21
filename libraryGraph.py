class Graph:

    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.grafo = []
        for i in range(self.vertices):
            linha = [["",0.0]] * self.vertices
            self.grafo.append(linha)
        self.directed = directed

    def adiciona_aresta(self, u, v, rotulo ,peso):
        self.grafo[u-1][v-1] = [rotulo, peso]
        self.grafo[v-1][u-1] = [rotulo, peso]

    def remove_aresta(self, u, v):
        self.grafo[u-1][v-1] = 0
        self.grafo[v-1][u-1] = 0

    

    def matriz_incidencia(self):
        matriz = [[0] * self.vertices for _ in range(self.vertices)]
        
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] != 0:
                    matriz[i][j] = 1


        return matriz

    def mostra_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

g = Graph(5,True)

g.adiciona_aresta(1, 2, 'A',1.0)
g.adiciona_aresta(1, 3,'B',2.0)
g.adiciona_aresta(1, 4,'C',3.0)


g.matriz_incidencia()
