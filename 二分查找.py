#普通查找方式为线性查找 从左到右挨个比对，因此时间复杂度为O(N)

def A(t,n):
    for i in range(len(t)):
        if t[i] == n:
            return True

    return False

#t = [1,2,3,4,5,6,7,8]

#print(A(t,5))

#二分查找
def B(t,n):
    left = 0
    right = len(t)-1
    while left<=right:
        m = int((left + right) / 2)
        if t[m]<n:
            left = m + 1
        elif t[m] >n:
            right = m - 1
        else:
            return True
    return False
#print(B(t,5))
#二分查找的时间复杂度为O(logN)
#使用递归方法进行二分查找
def C(t,n):
    left = 0
    right = len(t)-1
    if left<=right:
        mid = int((left+right)/2)
        if t[mid]<n:
            C(t[mid+1:],n)
        elif t[mid]>n:
            C(t[:mid-1],n)
        else:
            return True

    return False

#print(C(t,9))
import time
array = list(range(100000000))
t1 = time.time()
A(array,100000001)
t2 = time.time()
print('线性查找:',t2-t1)

t3 = time.time()
B(array, 100000001)
t4 = time.time()
print('二分查找：', t4 - t3)
