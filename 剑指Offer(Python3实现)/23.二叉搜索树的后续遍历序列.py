'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：二叉搜索树的特性是所有左子树值都小于中节点，所有右子树的值都大于中节点，递归遍历左子树和右子树的值。
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def IsPostTree(self,array):
        pass
