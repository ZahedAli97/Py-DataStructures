class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def insertNode(self, root, node):
        if root is None:
            root = node
        else:
            if root.data < node.data:
                if root.right is None:
                    root.right = node
                else:
                    self.insertNode(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insertNode(root.left, node)

    def deleteNode(self, root, data):
        if root.data < data:
            print("Hi from Right", end=" ")
            print("root: ", root.data, " data: ", data)
            # If Node has No Children
            if root.right.data == data and (root.right.right == None and root.right.left == None):
                root.right = None
            # If Node has One Child
            elif root.right.data == data and (root.right.right != None and root.right.left == None):
                root.right = root.right.right
            elif root.right.data == data and (root.right.right == None and root.right.left != None):
                root.right = root.right.left
            # If Node has Two Children
            elif root.right.data == data and (root.right.right != None and root.right.left != None):
                temp = root.right.data
                root.right.data = root.right.right.data
                root.right.right = None
                #self.deleteNode(root, data)
            else:
                self.deleteNode(root.right, data)
        else:
            print("Hi from Left", end=" ")
            print("root: ", root.data, " data: ", data)

            # If Node has No Children
            if root.left.data == data and (root.left.left == None and root.left.right == None):
                root.left = None
            # If Node has One Child
            elif root.left.data == data and (root.left.left != None and root.left.right == None):
                root.left = root.left.left
            elif root.left.data == data and (root.left.left == None and root.left.right != None):
                root.left = root.left.right
            # If Node has Two Children
            elif root.left.data == data and (root.left.left != None and root.left.right != None):
                temp = root.left.data
                root.left.data = root.left.right.data
                root.left.right = None
                #self.deleteNode(root, data)

            else:
                self.deleteNode(root.left, data)

    def mirror(self, root):
        if not root:
            return

        self.mirror(root.right)
        self.mirror(root.left)
        temp = root.left
        root.left = root.right
        root.right = temp

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data, "->", end=" ")
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        if root:
            print(root.data, "->", end=" ")
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            print(root.data, "->", end=" ")


if __name__ == "__main__":
    bst = BinarySearchTree(50)
    bst.insertNode(bst.root, Node(30))
    bst.insertNode(bst.root, Node(20))
    bst.insertNode(bst.root, Node(40))
    bst.insertNode(bst.root, Node(70))
    bst.insertNode(bst.root, Node(60))
    bst.insertNode(bst.root, Node(80))
    bst.inorderTraversal(bst.root)
    print("")  # For new Line
    bst.preorderTraversal(bst.root)
    print("")  # For new Line
    bst.postorderTraversal(bst.root)
    print("")  # For new Line
    bst.mirror(bst.root)
    bst.inorderTraversal(bst.root)
    print("")  # For new Line
    bst.preorderTraversal(bst.root)
    print("")  # For new Line
    bst.postorderTraversal(bst.root)
    print("")  # For new Line
    # print("Deleting Node with Two Children")
    # bst.deleteNode(bst.root, 70)
    # bst.inorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.preorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.postorderTraversal(bst.root)
    # print("")  # For new Line

    # bst.deleteNode(bst.root, 20)
    # bst.deleteNode(bst.root, 80)
    # print("After Deleting")
    # bst.inorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.preorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.postorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.deleteNode(bst.root, 70)
    # bst.deleteNode(bst.root, 30)
    # print("After Delteting Node with One Child!")
    # bst.inorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.preorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.postorderTraversal(bst.root)
    # print("")  # For new Line
    # print("Back to Original Manually")
    # bst.insertNode(bst.root, Node(30))
    # bst.insertNode(bst.root, Node(20))
    # bst.insertNode(bst.root, Node(70))
    # bst.insertNode(bst.root, Node(80))
    # bst.inorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.preorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.postorderTraversal(bst.root)
    # print("")  # For new Line

    # print("Deleting root Node")
    # bst.deleteNode(bst.root, 50)
    # bst.inorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.preorderTraversal(bst.root)
    # print("")  # For new Line
    # bst.postorderTraversal(bst.root)
    # print("")  # For new Line


# CORRECT ORDER FOR TRAVERSAL #
# 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 ->    INORDER
# 50 -> 30 -> 20 -> 40 -> 70 -> 60 -> 80 ->    PREORDER
# 20 -> 40 -> 30 -> 60 -> 80 -> 70 -> 50 ->    POSTORDER
