class Graph:

    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.grafo = []
        for i in range(self.vertices):
            linha = [[0,"",0.0]] * self.vertices
            self.grafo.append(linha)
        self.directed = directed

    def adiciona_aresta(self, u, v, rotulo ,peso):
        self.grafo[u-1][v-1] = [1,rotulo, peso]
        self.grafo[v-1][u-1] = [1,rotulo, peso]

    def remove_aresta(self, u, v):
        self.grafo[u-1][v-1] = 0
        self.grafo[v-1][u-1] = 0

    def raiz_incidencia(self):
        incidencia = [[0] * self.vertices for _ in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] != 0:
                    incidencia[i][j] = 1
        return incidencia

    def mostra_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem = [[-1, 0] for i in range(self.vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0:
            dist, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self.grafo[v-1][i]:
                        custo_vem[i] = [dist + self.grafo[v-1][i], v]
                        h.adiciona_no(dist + self.grafo[v-1][i], i+1)
        return custo_vem


g = Graph(5,True)

g.adiciona_aresta(1, 2, 'A',1.0)
g.adiciona_aresta(1, 3,'B',2.0)
g.adiciona_aresta(1, 4,'C',3.0)
g.adiciona_aresta(5, 5,'G',1.0)


g.mostra_matriz()
