from libraryGraph import Graph

def main():
    g = Graph(5)
    g.adiciona_aresta(1, 2, 1)
    g.adiciona_aresta(1, 3, 2)
    g.adiciona_aresta(1, 4, 3)
    g.adiciona_aresta(2, 3, 4)
    g.adiciona_aresta(2, 5, 5)
    g.adiciona_aresta(3, 4, 6)
    g.adiciona_aresta(4, 5, 7)
    g.mostra_matriz()
