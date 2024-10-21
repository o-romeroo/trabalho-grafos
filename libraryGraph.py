class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.arestas = [[] for _ in range(self.vertices)]
        self.arestas_retorno = []
        self.arestas_avanco = []
        self.arestas_cruzamento = []

    def adiciona_aresta(self, u, v, rotulo="", peso=0.0):
        aresta = Edge(u, v, rotulo, peso)
        self.arestas[u - 1].append(aresta)
        if not self.directed:
            aresta_inversa = Edge(v, u, rotulo, peso)
            self.arestas[v - 1].append(aresta_inversa)

    def remove_aresta(self, u, v):
        self.arestas[u - 1] = [aresta for aresta in self.arestas[u - 1] if aresta.v != v]
        if not self.directed:
            self.arestas[v - 1] = [aresta for aresta in self.arestas[v - 1] if aresta.v != u]

    def mostra_arestas(self):
        for i in range(self.vertices):
            print(f"Vértice {i + 1}: {self.arestas[i]}")

    def matriz_incidencia(self):
        matriz = [[0] * self.vertices for _ in range(self.vertices)]
        
        for i in range(self.vertices):
            for aresta in self.arestas[i]:
                matriz[i][aresta.v - 1] = 1

        return matriz

    def mostra_matriz(self):
        for i in range(self.vertices):
            print(self.grafo[i])

    def dfs(self, start):
        # Conjunto para armazenar os vértices visitados
        visited = set()
        # Dicionário para armazenar o tempo de descoberta e finalização
        discovery_time = {}
        finishing_time = {}
        # Contador de tempo
        time = [0]
        
        # Função recursiva interna para visitar os vértices
        def dfs_recursive(v):
            visited.add(v)
            time[0] += 1
            discovery_time[v] = time[0]
            
            # Itera sobre as arestas do vértice atual
            for edge in self.arestas[v - 1]:
                if edge.v not in visited:
                    # Aresta de árvore
                    dfs_recursive(edge.v)
                else:
                    # Verifica o tipo da aresta
                    if edge.v in discovery_time and edge.v not in finishing_time:
                        # Aresta de retorno: conecta um vértice a um de seus ancestrais
                        self.arestas_retorno.append(edge)
                    elif discovery_time[v] < discovery_time[edge.v]:
                        # Aresta de avanço: conecta um vértice a um descendente indireto
                        self.arestas_avanco.append(edge)
                    else:
                        # Aresta de cruzamento: conecta vértices de diferentes subárvores
                        self.arestas_cruzamento.append(edge)
            
            time[0] += 1
            finishing_time[v] = time[0]
    
        # Inicia a DFS a partir do vértice inicial
        dfs_recursive(start)


class Edge:
    def __init__(self, u, v, rotulo, peso):
        self.u = u
        self.v = v
        self.rotulo = rotulo
        self.peso = peso 

















# g = Graph(5,True)

# g.adiciona_aresta(1, 2, 'A',1.0)
# g.adiciona_aresta(1, 3,'B',2.0)
# g.adiciona_aresta(1, 4,'C',3.0)


# g.matriz_incidencia()
