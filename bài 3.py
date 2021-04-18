import numpy as np
m, n = map(int, input().split())#
arr=[int(i) for i in input().strip().split()[:m*n]]
a=np.array(arr) # chuyển từ list sang array numpy
#đưa numpy 1 chiều về 2 chiều gồm m hàng n cột
a=a.reshape(m,n)

p, q = map(int, input().split())#
arr=[int(i) for i in input().strip().split()[:p*q]]
b=np.array(arr)
b=b.reshape(p,q)

if n!=p :print("none\n")
else:
    res=np.matmul(a,b)#hàm nhân 2 ma trận
    print(res)