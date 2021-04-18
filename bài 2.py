import numpy as np
m, n = map(int, input().split())#
arr=[int(i) for i in input().strip().split()[:m*n]]
a=np.array(arr) # chuyển từ list sang array numpy
#đưa numpy 1 chiều về 2 chiều gồm m hàng n cột
a=a.reshape(m,n)
print( np.amax(a, axis=1) )# 1: ngang (hàng)
print( np.amin(a,axis=0))  #0 : đứng (cột)
# tổng đường chéo chính => các a[i][i] 
k=min(m,n)
res = sum(a[i][i] for i in range(k))
print(res)