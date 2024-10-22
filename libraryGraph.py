class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.arestas = [[] for _ in range(self.vertices)]
        self.arestas_retorno = []
        self.arestas_avanco = []
        self.arestas_cruzamento = []

    def adiciona_aresta(self, u, v, rotulo="", peso=0.0):
        if(u < 1 or u > self.vertices or v < 1 or v > self.vertices):
            raise ValueError("Vértice inválido")

        aresta = Edge(u, v, rotulo, peso)
        self.arestas[u - 1].append(aresta)
        if not self.directed:
            aresta_inversa = Edge(v, u, rotulo, peso)
            self.arestas[v - 1].append(aresta_inversa)

    def remove_aresta(self, origem, destino):
        if(origem < 1 or origem > self.vertices or destino < 1 or destino > self.vertices):
            raise ValueError("Vértice inválido")
        
        for aresta in enumerate(self.arestas):
            if(aresta[1].__len__()):
                for i in range(aresta[1].__len__()):
                    if(aresta[1][i].u == origem and aresta[1][i].v == destino):
                        del self.arestas[aresta[0]][i]
                        if(self.directed == False):
                            for aresta2 in enumerate(self.arestas):
                                if(aresta2[1].__len__()):
                                    for j in range(aresta2[1].__len__()):
                                        if(aresta2[1][j].u == destino and aresta2[1][j].v == origem):
                                            del self.arestas[aresta2[0]][j]
                                            break
        

                    

    def mostra_arestas(self):
        for i in range(self.vertices):
            if(self.arestas[i].__len__()):
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
            print(time, v)
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

    def __repr__(self):
        return f"({self.u}, {self.v}, {self.rotulo}, {self.peso})"



g = Graph(5, directed=False)

# Adicionando algumas arestas ao grafo
print("Adicionando arestas:")
g.adiciona_aresta(1, 2, 'A', 1.0)

print('Mostrando Arestas:')
g.mostra_arestas()
# g.adiciona_aresta(1,3, 'B', 1.0)
# g.adiciona_aresta(2,3, 'C', 1.0)


print('removendo Arestas:')
g.remove_aresta(1,2)


print('Mostrando Arestas:')
g.mostra_arestas()

# print("\nIniciando DFS a partir do vértice 1:")
# g.dfs(1)

# # Mostrando as arestas classificadas
# print("\nArestas de Retorno:", g.arestas_retorno)
# print("Arestas de Avanço:", g.arestas_avanco)
# print("Arestas de Cruzamento:", g.arestas_cruzamento)







