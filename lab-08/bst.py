class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
        self.deep = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.id = "root"
        self.height = 0
        self.visited = 0


    def insert(self, value):
        if(self.root == None):
            self.root = Node(value)
            self.root.deep = 1
            self.height = 1
            return
        
        curr_nd = self.root
        while True:
            if value < curr_nd.val:
                if curr_nd.left == None:
                    curr_nd.left = Node(value)
                    curr_nd.left.deep = curr_nd.deep + 1
                    self.height = max(self.height, curr_nd.left.deep)
                    break
                else: 
                    curr_nd = curr_nd.left
            elif value > curr_nd.val:
                if curr_nd.right == None:
                    curr_nd.right = Node(value)
                    curr_nd.right.deep = curr_nd.deep + 1
                    self.height = max(self.height, curr_nd.right.deep)
                    break
                else:
                    curr_nd = curr_nd.right
            else:
                break
    def fromArray(self, array):
        for i in array:
            if  isinstance(i, int):
                self.insert(i)
            else:
                raise ValueError("Invalid array element")

    def search(self, key):
        self.visited = 0
        if self.root == None:
            
            return False 
        node = self.root

        while node != None:
            self.visited += 1
            if key == node.val:
                return True
            elif(key < node.val):
                node = node.left
            else:
                node = node.right



        return False
    
    def min(self):
        if self.root == None:
            self.visited = 0
            return None
        curr_nd = self.root
        self.visited = 1
        while curr_nd.left != None:
            curr_nd = curr_nd.left
            self.visited += 1
        return curr_nd.val

    def max(self):
        if self.root == None:
            self.visited = 0
            return None
        self.visited = 1
        curr_nd = self.root
        while curr_nd.right != None:
            curr_nd = curr_nd.right
            self.visited += 1
        return curr_nd.val
    
    def visitedNodes(self):
        return self.visited

                
# bst = BinarySearchTree()
# values =[-5671, -3460, -279, -6226, -4709, -2759, 8146, 3171, 4951, 5025]
# # for v in values:
# #     bst.insert(v)
# bst.fromArray(values)

# print(bst.min())
# print(bst.max())
# # print(bst.search(7).deep)
# print(bst.visitedNodes())
# bst.__repr__().show()
    # def fromArray(self, array):
    #     pass

    # def search(self, value):
    #     pass

    # def min(self):
    #     pass

    # def max(self):
    #     pass

    # def visitedNodes(self):
    #     pass
