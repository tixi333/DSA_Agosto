from collections import deque

def in_order(node):
    actual = node
    if actual is None:
        return
    in_order(actual.l_child)
    print(actual.data)
    in_order(actual.r_child)

def pre_order(node):
    actual = node
    if actual is None:
        return
    print(actual.data)
    pre_order(actual.l_child)
    pre_order(actual.r_child)

def post_order(node):
    actual = node
    if actual is None:
        return
    post_order(actual.l_child)
    post_order(actual.r_child)
    print(actual.data)
    

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        if node.l_child:
            queue.append(node.l_child)
        if node.r_child:
            queue.append(node.r_child)
            
    return result
