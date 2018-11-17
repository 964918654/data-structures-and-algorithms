#二分法拓展
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
# 查找比如16在不在矩阵中。
A = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
def search(A,n):
    j = len(A[0])-1
    i = 0
    while i< len(A[0]) and j>=0:
        if A[i][j] == n:
            return True
        elif A[i][j]>n:
            j = j - 1
        else:
            i = i + 1
    return False

print(search(A,2))
print(search(A,50))