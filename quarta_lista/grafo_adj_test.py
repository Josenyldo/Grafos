import unittest
from quarta_lista.grafo_adj import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo([], [])

        for i in ['A','B','C','D']:
            self.g_p.adiciona_vertice(i)
        for i in ['A-B','B-D','D-C','C-B','C-D']:
            self.g_p.adiciona_aresta(i)

        self.g_p2 = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M']:
            self.g_p2.adiciona_vertice(i)
        for i in ['M-P', 'P-E', 'P-C', 'J-E', 'M-J']:
            self.g_p2.adiciona_aresta(i)


        self.g_c = Grafo([], [])
        for i in ['H', 'B', 'C','D','E','F']:
            self.g_c.adiciona_vertice(i)
        for i in ['B-H','C-D','F-E']:
            self.g_c.adiciona_aresta(i)






    def test_whashall(self):
        self.assertEqual(self.g_p.whashall(),[[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]])
        self.assertEqual(self.g_p2.whashall(), [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 1, 1, 1, 0]]);
        self.assertEqual(self.g_c.whashall(), [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0]])