def A1(A,a,b):
    c = a - 1
    d = A[b]
    for j in range(a,b):
        if A[j] <= d:
            c = c + 1
            A[c],A[j] = A[j],A[c]
    A[c+1],A[b] = A[b],A[c+1]
    return c+1
def A2(A,a,b):
    if a<b:
        c = A1(A,a,b)
        A2(A,a,c-1)
        A2(A,c+1,b)

A = [2,3,8,1,7,5,6,4]

A2(A,0,7)
print(A)