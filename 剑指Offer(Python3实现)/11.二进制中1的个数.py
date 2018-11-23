'''
题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

题解：每次进行左移一位，然后与1进行相与，如果是1则进行加1。
'''
class Solution:
    def numOf1(self,num):
        count = 0
        for i in range(32):
            count += (num >> i)&1
        return count

if __name__ == '__main__':
    solution = Solution()
    n = int(input())
    print(bin(n))
    a = solution.numOf1(n)
    print(a)