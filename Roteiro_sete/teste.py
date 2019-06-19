from Roteiro_sete.grafo_adj_nao_dir import *

g = Grafo()
for i in ['A', 'B', 'C', 'D']:
    g.adiciona_vertice(i)
for i in ['A-B', 'A-C', 'D-C', 'B-C', 'B-D']:
    g.adiciona_aresta(i)
g.DFS('A')