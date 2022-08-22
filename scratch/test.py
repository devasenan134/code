
class BST:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    
def insert(root, data):
    if root is None:
        return BST(data)
    else:
        if root.data == data:
            return root
        elif root.data < data:
            root.right = insert(root.right, data)
        elif root.data > data:
            root.left = insert(root.left, data)
    return root

def lvlOrder(root):
    if root:
        queue = [root]
    else:
        queue = []
    for node in queue:
        if node:
            print(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = BST(3)
root = insert(root, 5)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 1)
lvlOrder(root)


