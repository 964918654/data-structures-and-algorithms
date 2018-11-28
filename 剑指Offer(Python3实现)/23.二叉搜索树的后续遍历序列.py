'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：二叉搜索树的特性是所有左子树值都小于中节点，所有右子树的值都大于中节点，递归遍历左子树和右子树的值。
'''


class Solution:
    def IsPostTree(self,array):
        if not array:
            return False
        if len(array) == 1:
            return True
        i = 0
        while array[i]<array[-1]:
            i = i+1

        for j in range(i,len(array)-1):
            if array[j]<array[-1]:
                return False
        #print(i)
        leftarr = array[:i]
        #print(leftarr)
        rightarr = array[i:len(array)-1]
        #print(rightarr)



        if len(leftarr)>0:
            self.IsPostTree(leftarr)
        if len(rightarr)>0:
            self.IsPostTree(rightarr)
        return True

if __name__=='__main__':
    solution=Solution()
    num=list(map(int,input().split(' ')))

    ans=solution.IsPostTree(num)
    print(ans)
