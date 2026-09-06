import numpy as np
import matplotlib.pyplot as plt

x0=np.array([500,1000,500])
A=np.array([[0,5,4],[0.5,0,0],[0,0.25,0]])

N=10
x=np.zeros([3,N+1],dtype=int)
x[0,0]=500
x[1,0]=1000
x[2,0]=500
for t in range(N):
    x[0,t+1] = x[1,t]*4 + x[2,t]*3
    x[1,t+1] = x[0,t]*0.5
    x[2,t+1] = x[1,t]*0.25

T=N*5
print('第%d年的种群数量为：'%T)
print(x[0,N],x[1,N],x[2,N])

tt=np.linspace(start=0,stop=T,num=N+1)
plt.plot(tt,x[0,:],'bo-',label='0-5 years old')
plt.plot(tt,x[1,:],'go-',label='5-10 years old')
plt.plot(tt,x[2,:],'ro-',label='10-15 years old')
plt.legend(loc='upper left')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()