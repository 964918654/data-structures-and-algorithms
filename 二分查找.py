#普通查找方式为线性查找 从左到右挨个比对，因此时间复杂度为O(N)

def A(t,n):
    for i in range(len(t)):
        if t[i] == n:
            return True

    return False

t = [1,2,3,4,5,6,7,8]

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
            return m+1
    return False
print(B(t,7))
#二分查找的时间复杂度为O(logN)
#使用递归方法进行二分查找
def RecursiveBinarySearch(array, t):
    left = 0
    right = len(array) - 1

    if left>right:
        return False
    mid = int((left + right) / 2)
    if array[mid] < t:
        return RecursiveBinarySearch(array[mid+1:], t)
    elif array[mid] > t:
        return RecursiveBinarySearch(array[:mid], t)
    else:
        return mid
#并不能正确的返回值

def HalfSearch(OrderedList, key, left , right):
    if left > right:
        return None
    mid = (left + right) // 2
    if key == OrderedList[mid]:
        return mid
    elif key > OrderedList[mid]:
        return HalfSearch(OrderedList, key, mid + 1, right)
    else:
        return HalfSearch(OrderedList, key, left, mid - 1)


array = [1,2,3,4,5,6,7]
print(RecursiveBinarySearch(array,6))
print(HalfSearch(array,3,0,6))

import time
array = list(range(1000000))
t1 = time.time()
A(array,100001)
t2 = time.time()
print('线性查找:',t2-t1)

t3 = time.time()
HalfSearch(array, 100000000,0,999999)
t4 = time.time()
print('二分查找：', t4 - t3)
