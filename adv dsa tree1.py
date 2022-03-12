#Implement Binary tree
'''Create a class called Tree and initialize a constructor for passing the root value.
Then create a function in the class called insert for taking new nodes as input.
Now, the new input node checks with root value. The new input node 11 is less than 20, so it moves towards the left side of 20.
Another new input node 25 is greater than 20, so it moves towards the right side of 20.'''
class Tree:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def getTree(self):
        if self.left:
            self.left.getTree()
        print( self.data),
        if self.right:
            self.right.getTree()

root = Tree(20)
root.insert(11)
root.insert(25)
root.insert(10)
root.insert(30)
root.insert(19)

root.getTree()
