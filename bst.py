
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
                return current.data
            
            if data > current.data:
                
                if current.r_child == None:
                    return "no data"
                else:
                    
                    current = current.r_child
            
            if data < current.data:    
                if current.l_child == None:
                    return "no data"
                else:
                                    
                    current = current.l_child
                    
    def remove(self,data):
        pass

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