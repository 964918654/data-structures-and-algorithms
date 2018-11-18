#就是快速排序
def A(a,p,x):
    j=p-1
    n=a[x]
    for i in range(p,x):
        if a[i]<=n:
            j = j + 1
            a[i],a[j]=a[j],a[i]
    a[j+1],a[x] = a[x],a[j+1]
    return j+1

def B(a,p,x,k):
    if p<=x:
        y = A(a,p,x)
        if k-1 == y:
            return a[y]
        elif k-1>y:
            return B(a,y+1,x,k)
        else:
            return B(a,p,y-1,k)

a = [2, 8, 7, 1, 3, 5, 6, 4]

b = B(a,0,7,8)
print(b)