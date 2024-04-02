RED = 'RED'
BLACK = 'BLACK'

class RedBlackTreeNode:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)
        self.root.color = BLACK

    def _insert_recursive(self, node, key):
        if not node:
            return RedBlackTreeNode(key)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def _is_red(self, node):
        if not node:
            return False
        return node.color == RED



# Create a RedBlackTree instance
rb_tree = RedBlackTree()

# Insert some keys into the tree
keys = [50, 30, 70, 20, 40, 60, 80]
for key in keys:
    rb_tree.insert(key)

# Print the inorder traversal of the tree
def inorder_traversal_rb(node):
    if node:
        inorder_traversal_rb(node.left)
        print(node.key, end=' ')
        inorder_traversal_rb(node.right)

print("Inorder traversal of Red-Black Tree:")
inorder_traversal_rb(rb_tree.root)

