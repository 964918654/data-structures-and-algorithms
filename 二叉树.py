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
    if tree==None:
        return
    print(tree.val)
    preorder(tree.left)
    preorder(tree.right)
print(preorder(tree))
#结果示例：1 2 4 5 3 6 7

#后序遍历（先遍历左子树，再遍历右子树，最后遍历根节点）
def postorder(tree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.val)

print(postorder(tree))
#结果示例：4 5 2 6 7 3 1

#例题
#已知一颗二叉树的先序遍历序列为ABCDEFG，中序遍历为CDBAEGF，能否唯一确定一颗二叉树？如果可以，请画出这颗二叉树。
'''
            A
           / \
          B   E
         /     \
        C       F
         \     /
          D   G

    先序遍历: ABCDEFG
    中序遍历: CDBAEGF
    后序遍历: DCBGFEA
'''
# def buildTree(preorder,inorder):
#     if len(preorder) == 0:
#         return None
#     if len(preorder) == 1:
#         return TreeNode(preorder[0])
#     #拿出当前前序排列的节点str的第一个节点
#     root = TreeNode(preorder[0])
#     #根据拿到的节点得到该节点在中序排列中的下标位置
#     index = inorder.index(root.val)
#     #拿到左子树
#     root.left = buildTree(preorder[1:index+1],inorder[0:index])
#     #拿到右子树
#     root.right = buildTree(preorder[index+1:len(preorder)],inorder[index+1:len(inorder)])
#
#     return root
def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = buildTree(preorder[1 : index + 1], inorder[0 : index])
    root.right = buildTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
    return root

preorder_string = 'ABCDEFG'
inorder_string = 'CDBAEGF'

r = buildTree(preorder_string,inorder_string)

print(preorder(r))
print(inorder(r))
print(postorder(r))