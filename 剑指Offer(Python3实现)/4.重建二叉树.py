# 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
#
# 题解：首先前序遍历的第一个元素为二叉树的根结点，那么便能够在中序遍历之中找到根节点，
# 那么在根结点左侧则是左子树，假设长度为M.在根结点右侧，便是右子树,假设长度为N。
# 然后在前序遍历根节点后面M长度的便是左子树的前序遍历序列，再后面的N个长度便是右子树的后序遍历的长度。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:index+1],tin[0:index])
        root.right = self.reConstructBinaryTree(pre[index+1:len(pre)],tin[index+1:len(tin)])
        return root

if __name__=='__main__':
    solution =Solution()
    pre = list(map(int,input("请输入二叉树的前序排列:").split(',')))
    tin = list(map(int,input("请输入二叉树的中序排列:").split(',')))
    r = solution.reConstructBinaryTree(pre,tin)
    print(r)