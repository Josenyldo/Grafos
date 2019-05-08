from terceira_lista.grafo_adj_nao_dir import Grafo

g_c_e = Grafo()
for i in ['A', 'B', 'C']:
    g_c_e.adiciona_vertice(i)
for i in ['A-B', 'B-C']:
    g_c_e.adiciona_aresta(i)

print(g_c_e)
#print(g_c_e)