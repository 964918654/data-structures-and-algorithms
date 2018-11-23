'''
题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。n<=39。

题解：递归和迭代方法。
'''

class Solution:
    def Fibonacci1(self,n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            return self.Fibonacci1(n-1)+self.Fibonacci1(n-2)


    def Fibonacci2(self,n):
        if n == 0:
            return 0
        res = [0 for i in range(n+1)]
        res[1]=1
        res[0]=0
        for i in range(2,n+1):
            res[i] = res[i-1]+res[i-2]
        return res[n]




if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    a = solution.Fibonacci1(n)
    print(a)
    b = solution.Fibonacci2(n)
    print(b)
