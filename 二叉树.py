#二叉树的代码实现
"""
    1
  /  \
 2    3
"""
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)


#中序遍历（先遍历左子树，再遍历根节点，最后遍历右子树）
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
"""
     1
    / \ 
   2   3
  / \ / \ 
 4  5 6  7
"""
def inorder(tree):
    if tree:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)
print(inorder(tree))
#结果示例：4 2 5 1 6 3 7

#先序遍历（先遍历根节点，再遍历左子树，最后遍历右子树）
def preorder(tree):
    if tree:
        print(tree.val)
        inorder(tree.left)
        inorder(tree.right)
print(preorder(tree))
#结果示例：1 4 2 5 6 3 7

#后序遍历（先遍历左子树，再遍历右子树，最后遍历根节点）
def postorder(tree):
    if tree:
        inorder(tree.left)
        inorder(tree.right)
        print(tree.val)
print(postorder(tree))
#结果示例：4 2 5 6 3 7 1