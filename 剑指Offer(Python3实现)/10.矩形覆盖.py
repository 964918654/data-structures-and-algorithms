"""
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

题解：新增加的小矩阵竖着放，则方法与n-1时相同，新增加的小矩阵横着放，则方法与n-2时相同，于是f(n)=f(n-1)+f(n-2)。
ps:fibonacci

"""
class Solution:
    def rectCover(self,number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        res = [0 for i in range(number+1)]
        res[1] = 1
        res[2] = 2
        for i in range(3,number+1):
            res[i] = res[i-1]+res[i-2]
        return res[number]

if __name__=='__main__':
    solution=Solution()
    n=int(input())
    ans=solution.rectCover(n)
    print(ans)