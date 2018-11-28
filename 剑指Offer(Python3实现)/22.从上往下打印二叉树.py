'''
题目：从上往下打印出二叉树的每个节点，同层节点从左至右打印。

思路：递归，每次将左子树结果和右子树结果存到结果集之中。
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def PrintTree(self,root):
        array = []
        if root is None:
            return []
        array.append(root.val)
        self.orderarr(root,array)
        return array
    def orderarr(self,root,array):
        if not root:
            return
        if root.left:
            array.append(root.left.val)
        if root.right:
            array.append(root.right.val)
        self.orderarr(root.left,array)
        self.orderarr(root.right,array)

if __name__=='__main__':
    solution=Solution()
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    ans=solution.PrintTree(A1)
    print(ans)
