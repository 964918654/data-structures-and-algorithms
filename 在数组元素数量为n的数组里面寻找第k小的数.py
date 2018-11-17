def A(a,p,x):
    j=p-1
    n=a[x]
    for i in range(a(p,x)):
        if a[j]<=n:
            j = j + 1
            a[i],a[j]=a[j],a[i]
    a[j+1],a[x] = a[x],a[j+1]
    return j+1

