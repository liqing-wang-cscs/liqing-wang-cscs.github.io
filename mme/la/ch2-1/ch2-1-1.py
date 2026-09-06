import numpy as np

N=21
myF=np.zeros(N,dtype=int)
myF[0]=1
myF[1]=1
for k in range(2,N):
    myF[k]=myF[k-1]+myF[k-2]

print(myF)