vertex_data = ['A', 'B', 'C', 'D']

adj_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0], 
    [1, 1, 0, 0], 
    [1, 0, 0, 0]  
]

def printMatrix(matrix):
    print("\nMatriz:")
    for i in matrix:
        print(i)

def printConnections(matrix, vertices):
    print("\nConexiones por nodo:")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()

print('Nodos:',vertex_data)
printMatrix(adj_matrix)

printConnections(adj_matrix, vertex_data)