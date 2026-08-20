from collections import deque
from funciones import *

class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None


raiz = Nodo("*") 

nodoa= Nodo(8)
nodob = Nodo("-") 

nodoc = Nodo("/") 
nodod = Nodo(9) 
nodoe = Nodo(2) 

nodof =Nodo ("+")
nodog = Nodo(2)
nodoh = Nodo(6)

raiz.l_child = nodoc
raiz.r_child = nodob

nodob.l_child = nodod
nodob.r_child= nodoe

nodoc.l_child = nodof
nodoc.r_child = nodoa

nodof.l_child = 2
nodof.r_child = 6