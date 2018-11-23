'''
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

题解：遍历数组寻找数组最小值。

'''
class Solution:
    def minNumberInArray(self,array):
        minnum = 9999999999
        for i in range(len(array)):
            if minnum>array[i]:
                minnum = array[i]

        if minnum:
            return minnum
        else:
            return 0

if __name__ == '__main__':
    solution = Solution()
    array = list(map(int,input("请输入一个旋转数组:").split(',')))
    num = solution.minNumberInArray(array)
    print(num)