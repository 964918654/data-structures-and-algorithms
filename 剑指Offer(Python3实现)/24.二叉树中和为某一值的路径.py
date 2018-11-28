'''
题目：输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)。

思路：利用递归的方法，计算加左子树和右子树之后的值，当参数较多是，可以将结果添加到函数变量之中。

'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self,root,num):
        if not root:
            return []
        ans = []
        path = []
        self.addpath(root,num,ans,path)
        ans.sort()
        return ans
    def addpath(self,root,num,ans,path):
        if not root:
            return
        path.append(root.val)
        if root.left is None and root.right is None and root.val == num:
            ans.append(path[:])

        if root.left:
            self.addpath(root.left,num-root.val,ans,path)
        if root.right:
            self.addpath(root.right,num-root.val,ans,path)

        path.pop()

if __name__=='__main__':
    A1=TreeNode(10)
    A2=TreeNode(8)
    A3=TreeNode(12)
    A4=TreeNode(4)
    A5=TreeNode(2)
    A6=TreeNode(2)

    A1.left=A2
    A1.right=A3
    A2.left=A4
    A2.right=A5
    A5.left=A6

    expectNumber=22
    solution=Solution()
    ans=solution.FindPath(A1,expectNumber)
    print(ans)
