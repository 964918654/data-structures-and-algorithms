#普通查找方式为线性查找 从左到右挨个比对，因此时间复杂度为O(N)

def A(t,n):
    for i in range(len(t)):
        if t[i] == n:
            return True

    return False

t = [1,2,3,4,5,6,7,8]

print(A(t,5))

#二分查找
def B(t,n):
    left = 0
    right = len(t)-1
    while left<=right:
        m = (t[left] + t[right])/2
        if m<n:
            left = left + 1
        elif m >n:
            right = right - 1
        else:
            return True
    return False
print(B(t,9))



