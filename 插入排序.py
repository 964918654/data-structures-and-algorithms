def insertSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]> key:
            A[i+1]=A[i]
            i = i-1
        A[i+1]=key
    return A

A = [2,1,4,3,7,5,6]
insertSort(A)
print(A)
#嵌套循环，因此时间复杂度为O(N²)