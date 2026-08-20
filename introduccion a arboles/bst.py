
class Nodo:
    def __init__(self, data):
        self.data = data
        self.r_child = None
        self.l_child = None

class BinaryTreeSearch:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Nodo(data)
        if self.root == None:
            self.root = node
            return

        current = self.root
        while True:
            if current.data > node.data:
                if current.l_child is None:
                    current.l_child = node
                    return
                else:
                    current = current.l_child

            else:
                if current.r_child is None:
                    current.r_child = node
                    return
                else:
                    current = current.r_child

    def find_max(self):
        if self.root.data == None:
            return
        
        current = self.root
        while True:
            if current.r_child == None:
                return current
            else:
                current = current.r_child

    def find_min(self):
        if self.root.data == None:
            return
        
        current = self.root
        while True:
            if current.l_child == None:
                return current
            else:
                current = current.l_child

    def search(self, data):
        if self.root == None:
            return "No hay nodo para realizar la busqueda"
        
        current = self.root
        
        while True:
            
            if data == current.data:
                return current
            
            if data > current.data:
                
                if current.r_child == None:
                    return None
                else:
                    
                    current = current.r_child
            
            if data < current.data:    
                if current.l_child == None:
                    return None
                else:
                                    
                    current = current.l_child
    
    def get_node_parent(self, data):
        current = self.root
        parent = None
        while current:
            if current.data == data:
                return current, parent
            parent = current
            if data < current.data:
                current= current.l_child
            else:
                current = current.r_child
        return None, None     
       
    def get_successor(self, node):
        current = node.r_child

        while current.l_child is not None:
            current = current.l_child

        return current
    
    def remove(self,data):
        node, parent = self.get_node_parent(data)
        
        if node is None and parent is None:
            return False
        
        children_count = 0
        
        if node.r_child and node.l_child:
            children_count = 2
        elif node.r_child or node.l_child:
            children_count = 1
        
        if children_count == 0:
            if parent == None:
                self.root == None
            
            elif parent.l_child == node:
                parent.l_child = None
            
            else:
                parent.r_child = None
                
            return True
        
        elif children_count == 1:
            if parent == None:
                if node.l_child:
                    self.root = node.l_child
                else:
                    self.root = node.r_child
            
            else:
                if parent.l_child is node:
                    if node.l_child:
                        parent.l_child = node.l_child
                    else:
                        parent.l_child = node.r_child
                else:
                    if node.l_child:
                        parent.r_child = node.l_child
                    else:
                        parent.r_child = node.r_child
            return True
        else:
            
            sucesor = self.get_successor(node)
            self.remove(sucesor.data)
            node.data = sucesor.data
                    
            return True

bst = BinaryTreeSearch()
bst.insert(3)
bst.insert(7)
bst.insert(2)
max = bst.find_max()
print(max.data)
min = bst.find_min()
print(min.data)
val = bst.search(8)
print(val)
removed = bst.remove(2)
print(removed)
"""""
    def insert_loop(self,data):
        pass

    def insert_recursive(self,data):
        node = Nodo(data)
        if self.root.data == None:
            self.root = node
            return
        else:
            _insert_recursive(self.root,node)
        

    def _insert_recursive(self,node,data):
        if node.data > data:
            if node.left is None:
                node.left =data
            else:
                _insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right =data
            else:
                _insert_recursive(node.right, data)
"""""