from collections import deque
vertex = ['A','B','C','D']
adj = {
    'A' : ['B','C','D'],
    'B' : ['A','C'],
    'C' : ['A','B'],
    'D' : ['A','E'],
    'E' : ['D']
}

def bfs(adj, inicio):
    
    visitados = []
    queue = deque()
    
    queue.append(inicio)
    visitados.append(inicio)
    
    while queue:
        actual = queue.popleft()
        print(actual)
        
        for c in adj[actual]:
            if c not in visitados:
                queue.append(c)
                visitados.append(c)
                
bfs(adj, 'A')
print()

def dfs(adj, inicio):
    visitados = []
    stack = []

    stack.append(inicio)

    while stack:
        actual = stack.pop()

        if actual not in visitados:
            visitados.append(actual)
            print(actual)

            for c in adj[actual]:
                if c not in visitados:
                    stack.append(c)
                    
dfs(adj,'A')