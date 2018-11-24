'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）。

题解：将树转变为中序序列，然后转变为str类型，最后判断是否包含。
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self,tree,array):
        if not tree:
            return
        self.inorder(tree.left,array)
        array.append(tree.val)
        self.inorder(tree.right,array)

    def HasTree(self,a,b):
        if a is None or b is None:
            return False
        arrayA,arrayB = [],[]
        self.inorder(a,arrayA)
        self.inorder(b,arrayB)
        strA = ''.join(str(i) for i in arrayA)
        strB = ''.join(str(i) for i in arrayB)

        if strB in strA:
            return True
        else:
            return False

if __name__=='__main__':
    solution=Solution()
    pRootA1 = TreeNode(1)
    pRootA2 = TreeNode(2)
    pRootA3 = TreeNode(3)
    pRootA4 = TreeNode(4)
    pRootA5 = TreeNode(5)
    pRootA1.left=pRootA2
    pRootA1.right=pRootA3
    pRootA2.left=pRootA4
    pRootA2.right=pRootA5

    pRootB2 = TreeNode(2)
    pRootB4 = TreeNode(4)
    pRootB5 = TreeNode(5)
    pRootB2.left=pRootB4
    pRootB2.right = pRootB5
    ans=solution.HasTree(pRootA1,pRootB2)
    print(ans)
