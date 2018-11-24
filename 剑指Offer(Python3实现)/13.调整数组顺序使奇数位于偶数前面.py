'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

题解：申请奇数数组和偶数数组，分别存放奇数值和偶数值，数组相加便为结果。
'''
class Solution:
    def reOrderArray(self,array):
        array1 = []
        array2 = []
        for i in range(len(array)):
            if array[i]%2 == 0:
                array1.append(array[i])
            else:
                array2.append(array[i])
        array0 = array2+array1
        return array0

if __name__ == '__main__':
    solution = Solution()
    array = list(map(int,input().split(',')))
    ans = solution.reOrderArray(array)
    print(ans)