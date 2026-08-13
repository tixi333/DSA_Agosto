
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
        if self.root.data == None:
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

    def find_max(self):
        pass

    def find_min(self):
        pass

    def search(self):
        pass

bst = BinaryTreeSearch()
bst.insert(3)
bst.insert(7)