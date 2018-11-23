'''
题目：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
class Solution:
    def numP(self,base,exponent):
        res = 1
        for i in range(abs(exponent)):
            res = res*base

        if exponent>0:
            return res
        else:
            return 1/res

if __name__ == '__main__':
    solution = Solution()
    base = float(input())
    exponent = int(input())
    a = solution.numP(base, exponent)
    print(a)