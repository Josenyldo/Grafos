from terceira_lista.grafo_adj_nao_dir import Grafo

g_c_e = Grafo()
for i in ['M', 'T', 'B', 'R']:
    g_c_e.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
    g_c_e.adiciona_aresta(i)

print(g_c_e.busca_grafo())
print(g_c_e)