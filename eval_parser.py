from clase_nodo import Nodo
from funciones import *

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = self.items[-1]
        return last
    
    def is_empty(self):
        return True if self.items == [] else False
    
    def size(self):
        size = len(self.items)
        return size
    
def calc (node):

    if node.data == "+":
        return calc (node.l_child) + calc(node.r_child)
    elif node.data == "-":
        return calc (node.l_child) - calc(node.r_child)
    elif node.data == "*":
        return calc (node.l_child) * calc(node.r_child)
    elif node.data == "/":
        return calc (node.l_child) / calc(node.r_child)
    else:
        return node.data

def parser (exp):
    stack = Stack()
    conj = exp.split()
    for e in conj:
        
        nodo = Nodo(e)
        if e in "+-*/":
            nodo.r_child = stack.pop()
            nodo.l_child = stack.pop()
            stack.push(nodo)
        else:
            stack.push(nodo)
    return stack.pop()

expresion = "22 7 - 4 * 5 + 5 2 - /"
arbol = parser(expresion)
print(calc(arbol))