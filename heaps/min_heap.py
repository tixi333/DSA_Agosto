
def main(MinHeap):
    minheap = MinHeap()
    minheap.insert(5)
    minheap.insert(2)
    minheap.insert(4)
    minheap.insert(8)
    minheap.insert(7)
    minheap.insert(9)
    minheap.insert(10)
    
    print(minheap.heap_sort())

    print(minheap.delete_at_location(3))
    print(minheap.delete_at_root())


    
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self,data):
        self.heap.append(data)
        self.arrange(len(self.heap)-1)
    
    def delete_at_root(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.sink(0)

        return root
    
    def delete_at_location(self,location):
        if location < 0 or location >= len(self.heap):
            return

        deleted = self.heap[location]
        last = self.heap.pop()

        if location < len(self.heap):
            self.heap[location] = last

            if location > 0:
                parent = (location - 1) // 2

                if self.heap[location] < self.heap[parent]:
                    self.arrange(location)
                else:
                    self.sink(location)
            else:
                self.sink(location)

        return deleted

    def heap_sort(self):
        copy_heap = MinHeap()
        copy_heap.heap = self.heap.copy()
        
        sorted_list = []
        
        while len(copy_heap.heap) > 0:
            sorted_list.append(copy_heap.delete_at_root())
        
        return sorted_list
    
    def arrange(self, location):
        
        while location > 0:
            
            parent = (location - 1) // 2
            
            if self.heap[parent] > self.heap[location]:
                self.heap[parent], self.heap[location] = self.heap[location], self.heap[parent]
                
                location = parent
                
            else:
                return

    def sink(self, location):
        left = 2 * location + 1
        
        while left < len(self.heap):
            
            child = self.minchild(location)
            if self.heap[location] > self.heap[child]:
                self.heap[child], self.heap[location] = self.heap[location], self.heap[child]
                
                location = child
                left = 2 * location + 1
                
            else:
                return

    def minchild(self, location):
        parent = location
        left = 2 * parent + 1
        right = 2* parent + 2
        
        if right >= len(self.heap):
            return left
    
        if self.heap[left] < self.heap[right]:
            return left
        else:
            return right
        
main(MinHeap)

#parent = (i - 1) // 2
#left = 2 * i + 1
#right = 2 * i + 2