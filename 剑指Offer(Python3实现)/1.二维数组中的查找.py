# 题目： 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 思路：遍历每一行，查找该元素是否在该行之中
class Solution:
    def Find(self,target,array):
        m = len(array)
        n = len(array[0])
        for i in range(m):
            for j in range(n):
                if array[i][j] == target:
                    return True


        return False
array = [
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,6]
]
a = Solution()
print(a.Find(7,array))
print(a.Find(1,array))
print(a.Find(0,array))