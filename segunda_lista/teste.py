from segunda_lista.grafo_adj_nao_dir import Grafo

g = Grafo()
g.adicionaVertice('J')
g.adicionaVertice('C')
g.adicionaVertice('E')
g.adicionaVertice('P')
g.adicionaVertice('M')
g.adicionaVertice('T')
g.adicionaVertice('Z')
g.adicionaAresta('J-C')
g.adicionaAresta('C-E')
g.adicionaAresta('C-E')
g.adicionaAresta('C-P')
g.adicionaAresta('C-P')
g.adicionaAresta('C-M')
g.adicionaAresta('C-T')
g.adicionaAresta('M-T')
g.adicionaAresta('T-Z')
print(g.arestas_sobre_vertice("J"))
