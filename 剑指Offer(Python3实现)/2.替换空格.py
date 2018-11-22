# 题目： 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 思路：利用字符串中的replace直接替换即可。
class Solution:
    def replaceSpace(self,val):
        temp = val.replace(" ","%20")
        return temp

a = Solution()
print(a.replaceSpace('We Are Happy'))