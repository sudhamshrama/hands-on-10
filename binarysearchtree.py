class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if not node.left:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if not node.right:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)



# Create a BinarySearchTree instance
bst = BinarySearchTree()

# Insert some keys into the tree
keys = [50, 30, 70, 20, 40, 60, 80]
for key in keys:
    bst.insert(key)

# Print the inorder traversal of the tree
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

print("Inorder traversal of Binary Search Tree:")
inorder_traversal(bst.root)

