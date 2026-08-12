from collections import deque
from funciones import *

class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

raiz = Nodo('A')
nodo_b = Nodo('B')
nodo_c = Nodo('C')
nodo_d = Nodo('D')
nodo_e = Nodo('E')
nodo_f = Nodo('F')
nodo_g = Nodo('G')

raiz.l_child = nodo_b
raiz.r_child = nodo_f

nodo_b.l_child = nodo_c
nodo_b.r_child = nodo_e

nodo_c.l_child = nodo_d

nodo_f.l_child = nodo_g

print("In order")
in_order(raiz)
print("Post order")
post_order (raiz)
print("Pre order")
pre_order(raiz)

print("Level order")
result = level_order(raiz)
print(result)
