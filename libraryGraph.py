class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed
        self.arestas = [[] for _ in range(len(self.vertices))]
        self.arestas_retorno = []
        self.arestas_avanco = []
        self.arestas_cruzamento = []

    def adiciona_aresta(self, origem, destino, rotulo="", peso=0.0):
        if origem not in self.vertices or destino not in self.vertices:
            raise ValueError("Vértice inválido")

        origem_idx = self.vertices.index(origem)
        destino_idx = self.vertices.index(destino)

        aresta = Edge(origem_idx + 1, destino_idx + 1, rotulo, peso)
        self.arestas[origem_idx].append(aresta)
        if not self.directed:
            aresta_inversa = Edge(destino_idx + 1, origem_idx + 1, rotulo, peso)
            self.arestas[destino_idx].append(aresta_inversa)

    def remove_aresta(self, origem, destino):
        if origem not in self.vertices or destino not in self.vertices:
            raise ValueError("Vértice inválido")
        
        origem_idx = self.vertices.index(origem)
        destino_idx = self.vertices.index(destino)

        for aresta in self.arestas[origem_idx]:
            if aresta.v == destino_idx + 1:
                self.arestas[origem_idx].remove(aresta)
                break

        if not self.directed:
            for aresta in self.arestas[destino_idx]:
                if aresta.v == origem_idx + 1:
                    self.arestas[destino_idx].remove(aresta)
                    break

    def mostra_arestas(self):
        for i, vertex in enumerate(self.vertices):
            if len(self.arestas[i]) > 0:
                print(f"Vértice {vertex.rotulo} (Índice {i + 1}): {self.arestas[i]}")

    def matriz_incidencia(self):
        matriz = [[0] * len(self.vertices) for _ in range(len(self.vertices))]
        
        for i in range(len(self.vertices)):
            for aresta in self.arestas[i]:
                matriz[i][aresta.v - 1] = 1

        return matriz

    def mostra_matriz(self):
        matriz = self.matriz_incidencia()
        for row in matriz:
            print(row)

    def dfs(self, start):
        if start not in self.vertices:
            raise ValueError("Vértice inicial inválido")

        visited = set()
        discovery_time = {}
        finishing_time = {}
        time = [0]

        def dfs_recursive(v):
            visited.add(v)
            time[0] += 1
            discovery_time[v] = time[0]
            print(f"Visitando {v.rotulo}, tempo de descoberta: {time[0]}")

            v.visitado = True

            v_idx = self.vertices.index(v)
            for edge in self.arestas[v_idx]:
                next_vertex = self.vertices[edge.v - 1]
                if next_vertex not in visited:
                    dfs_recursive(next_vertex)
                else:
                    if next_vertex in discovery_time and next_vertex not in finishing_time:
                        self.arestas_retorno.append(edge)
                    elif discovery_time[v] < discovery_time[next_vertex]:
                        self.arestas_avanco.append(edge)
                    else:
                        self.arestas_cruzamento.append(edge)

            time[0] += 1
            finishing_time[v] = time[0]
            print(f"Finalizando {v.rotulo}, tempo de término: {time[0]}")
    
        dfs_recursive(start)


class Edge:
    def __init__(self, origem, destino, rotulo, peso):
        self.origem = origem
        self.v = destino
        self.rotulo = rotulo
        self.peso = peso 

    def __repr__(self):
        return f"({self.origem}, {self.v}, {self.rotulo}, {self.peso})"

class Vertex:
    def __init__(self, rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.processado = False

    def __repr__(self):
        return f"{self.rotulo}"


# Criando vértices
v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")
v5 = Vertex("E")

# Criando um grafo usando os vértices
g = Graph([v1, v2, v3, v4, v5], directed=True)

# Adicionando arestas
g.adiciona_aresta(v1, v5, "aresta_1", 1.0)

g.mostra_arestas()

g.remove_aresta(v1, v5)

g.mostra_arestas()
# g.adiciona_aresta(v1, v3, "aresta_2", 2.0)
# g.adiciona_aresta(v2, v4, "aresta_3", 3.0)
# g.adiciona_aresta(v3, v5, "aresta_4", 4.0)

# Mostrando arestas
# g.mostra_arestas()

# # Executando a DFS a partir do vértice A
# g.dfs(v1)
