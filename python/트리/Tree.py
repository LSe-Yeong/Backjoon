class node:
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root is None:
            self.root = node(value,None,None)
        else:
            self.add_insert(self.root,value)
            
    def add_insert(self,cur,value):
        if value < cur.value:
            if cur.left is None:
                cur.left = node(value,None,None)
            else:
                self.add_insert(cur.left,value) 
        else:
            if cur.right is None:
                cur.right = node(value,None,None)
            else:
                self.add_insert(cur.right,value) 
    
    def search(self,value):
        cur_node = self.root
        while True:
            if cur_node.value == value:
                return True
            elif cur_node.value > value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            if cur_node is None:
                return False

    def inOrder(self,node):
        if node is not None:
            self.inOrder(node.left)
            print(node.value,end=" ")
            self.inOrder(node.right)
    
    def preOrder(self,node):
        if node is not None:
            print(node.value,end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def postOrder(self,node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.value,end=" ")
    
    def remove(self,value):
        self.root = self._remove(self.root,value)

    def _remove(self,cur,value):    
        if cur is None:
            return cur

        if cur.value < value:
            cur.right = self._remove(cur.right,value)
        elif cur.value > value:
            cur.left = self._remove(cur.left,value)
        else:
            if cur.left is None and cur.right is None:
                return None
            
            if cur.left is None:
                return cur.right
            elif cur.right is None:
                return cur.left
            
            min_value = self._find_min(cur.right)
            cur.value = min_value
            cur.right = self._remove(cur.right,min_value)
        
        return cur

    def _find_min(self,cur):
        while cur.left is not None:
            cur = cur.left
        return cur.value

tree = Tree()
values = [7,8,2,4,5,1,3,11]
for v in values:
    tree.insert(v)

print(tree.search(7))
print(tree.search(15))

tree.inOrder(tree.root)
print()
tree.preOrder(tree.root)
print()
tree.postOrder(tree.root)

tree.remove(11)
tree.remove(4)

print()
tree.inOrder(tree.root)
print()
tree.preOrder(tree.root)
print()
tree.postOrder(tree.root)

