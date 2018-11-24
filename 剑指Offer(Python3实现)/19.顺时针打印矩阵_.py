'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
 1 2 3 4
 5 6 7 8
 9 10 11 12
 13 14 15 16
则依次打印出数字
1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
思路：每次打印圈，但要判断最后一次是打印横还是竖，另外判断数据是否已存在。
'''
class Solution:
    def printCircle(self,matrix):
        m,n = len(matrix),len(matrix[0])
        res = []
        if m==1 and n==1:
            res.append(matrix[0][0])

        for k in range((min(m,n)+1)//2):
            [res.append(matrix[k][i]) for i in range(k,n-k)]
            [res.append(matrix[i][n-k-1]) for i in range(k,m-k) if matrix[i][n-k-1] not in res]
            [res.append(matrix[m-k-1][i]) for i in range(n-k-1,k,-1) if matrix[m-k-1][i] not in res]
            [res.append(matrix[i][k]) for i in range(m-k-1,k,-1) if matrix[i][k] not in res]
        return res


if __name__ == '__main__':

    solution = Solution()
    a = list(map(int,input("请输入一个列表：").split(" ")))
    print(a)
    n = int(input("每个小列表的长度:"))
    matrix = [a[i:i+n] for i in range(0,len(a),n)]

    print(matrix)
    ans = solution.printCircle(matrix)
    print(ans)