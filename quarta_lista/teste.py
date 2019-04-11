from quarta_lista.grafo_adj import *

g_p = Grafo()
for i in ['H', 'B', 'C','D','E','F']:
    g_p.adiciona_vertice(i)
for i in ['B-H','C-D','F-E']:
    g_p.adiciona_aresta(i)

print(g_p.whashall())
print(g_p)
