vertex = ['A','B','C','D']
adj = {
    'A' : ['B','C','D'],
    'B' : ['A','C'],
    'C' : ['A','B'],
    'D' : ['A']
}

def printList(lista):
    for a, b in lista.items():
        print(f"{a} : {b}")


print('Nodos:',vertex)
print()
printList(adj)