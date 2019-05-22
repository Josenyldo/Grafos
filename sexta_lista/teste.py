from sexta_lista.grafo_adj import *

g = Grafo()
for i in ['A','B','C','D','E']:
    g.adiciona_vertice(i)
for i in ['A-B','A-D','D-C','B-C','D-E','C-E']:
    print(i)
    peso = int(input('Peso: '))
    g.adiciona_aresta(i,peso)

print(g.Kruskal())
