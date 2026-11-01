vertex = ['A','B','C','D']
adj = {
    'A' : ['B','C','D'],
    'B' : ['A','C'],
    'C' : ['A','B'],
    'D' : ['A']
}
def list_to_matrix(lista, vertices):
    matriz = []

    for e in vertices:
        fila = []

        for v in vertices:
            if v in lista[e]:
                fila.append(1)
            else:
                fila.append(0)

        matriz.append(fila)

    return matriz


print(list_to_matrix(adj, vertex))