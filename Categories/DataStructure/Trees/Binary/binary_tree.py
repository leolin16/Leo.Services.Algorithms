class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# print trees in order
#           15
#       /       \
#      10       32
#    /    \     / \
#   1     12   17 39
#    \    / \     /
#     5  11 14   37
#    / \
#   4   7

# inorder means, everthing on the right side must printed out before the node, vise versa
def inorder(root):
    # recursion needs to be considered from the base cases
    if root == None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# search the binary search tree
# time complexity: O(logn)
def search(root, target):
    if root == None:
        return None
    if root.val == target:
        return root
    elif root.val < target:
        return search(root.right, target)
    else:
        return search(root.left, target)

def same_tree(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    elif root1.val != root2.val:
        return False
    return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

leaf1 = Node(4)
leaf2 = Node(7)
leaf3 = Node(11)
leaf4 = Node(14)
leaf5 = Node(37)
leaf6 = Node(17)

node1 = Node(5, leaf1, leaf2)
node2 = Node(12, leaf3, leaf4)
node3 = Node(39, leaf5, None)
node4 = Node(32, leaf6, node3)
node5 = Node(1, None, node1)
node6 = Node(10, node5, node2)
root = Node(15, node6, node4) # binary search tree: left is less than the parent, right is greater than the parent

inorder(root)

print(search(root, 37).val)
print(search(root, 40))

root1 = Node(1, Node(2), Node(3))
root2 = Node(1, Node(2), Node(3))

root3 = Node(1, Node(2), None)
root4 = Node(1, None, Node(2))

root5 = Node(1, Node(2), Node(1))
root6 = Node(1, Node(1), Node(2))

print(same_tree(root1, root2))
print(same_tree(root3, root4))
print(same_tree(root5, root6))
