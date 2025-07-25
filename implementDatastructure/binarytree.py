class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        elif data >= current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def inorder_traversal(self):
        nodes = []
        self._inorder_recursive(self.root, nodes)
        return nodes

    def _inorder_recursive(self, node, nodes):
        if node:
            self._inorder_recursive(node.left, nodes)
            nodes.append(node.data)
            self._inorder_recursive(node.right, nodes)

    def preorder_traversal(self):
        nodes = []
        self._preorder_recursive(self.root, nodes)
        return nodes

    def _preorder_recursive(self, node, nodes):
        if node:
            nodes.append(node.data)
            self._preorder_recursive(node.left, nodes)
            self._preorder_recursive(node.right, nodes)

    def postorder_traversal(self):
        nodes = []
        self._postorder_recursive(self.root, nodes)
        return nodes

    def _postorder_recursive(self, node, nodes):
        if node:
            self._postorder_recursive(node.left, nodes)
            self._postorder_recursive(node.right, nodes)
            nodes.append(node.data)

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    print("Inorder Traversal:", tree.inorder_traversal())
    print("Preorder Traversal:", tree.preorder_traversal())
    print("Postorder Traversal:", tree.postorder_traversal())