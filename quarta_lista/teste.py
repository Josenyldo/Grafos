from quarta_lista.grafo_adj import *

g_p = Grafo([], [])
for i in ['A','B','C','D']:
    g_p.adiciona_vertice(i)
for i in ['A-B','B-D','D-C','C-B','C-D']:
    g_p.adiciona_aresta(i)
print(g_p)
print(g_p.whashall())
print(g_p)
