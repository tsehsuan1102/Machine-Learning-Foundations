
import numpy as np
from numpy import random
 
def sign(x):#自定义符号函数，只返回-1，+1
    ret=np.ones(x.shape)
    for i,each in enumerate(x):
        if each<0: ret[i]=-1
    return ret
 
def getTheta(x):#由输入的x生成假设空间的所有theta的序列
    n=len(x)
    l1=sorted(x)
    theta=np.zeros(n)
    for i in range(n-1):
        theta[i]=(l1[i]+l1[i+1])/2
    theta[-1]=1
    return theta
    
def q17_18():
    data_size=20
    expes=5000
    E_in=0
    E_out=0
    for i in range(expes):
        x=random.uniform(-1,1,data_size)
        noise_rate=0.2
        #生成[-0.2,0.8]范围内的随机数组，取sign()即变为有20%的-1的随机数组
        noise=sign(random.uniform(size=data_size)-noise_rate)
        y=sign(x)*noise   #为y加上20%的噪声
        theta=getTheta(x)
        e_in=np.zeros((2,data_size))#对每个theta求出一个error_in,第一行是s=1，第2行是s=-1.
        for i in range(len(theta)):
            a1=y*sign(x-theta[i])
            e_in[0][i]=(data_size-np.sum(a1))/(2*data_size)#数组只有-1和+1，可直接计算出-1所占比例
            e_in[1][i]=(data_size-np.sum(-a1))/(2*data_size) 
        s=0;theta_best=0
        min0, min1 = np.min(e_in[0]), np.min(e_in[1])
        if min0<min1:
            s=1
            theta_best=theta[np.argmin(e_in[0])]
        else:
            s=-1
            theta_best=theta[np.argmin(e_in[1])]
        e_out=0.5+0.3*s*(np.abs(theta_best)-1)
        E_in+=np.min(e_in)
        E_out+=np.min(e_out)
    ave_in=E_in/expes
    ave_out=E_out/expes
    print(ave_in,ave_out)
 
def deciStump(x,y):#d:第d维,x:第x维数据 y：标签
    data_size=len(x)
    theta=getTheta(x)
    e_in=np.zeros((2,data_size))
    for i in range(len(theta)):
        a1=y*sign(x-theta[i])
        e_in[0][i]=(data_size-np.sum(a1))/(2*data_size)
        e_in[1][i]=(data_size-np.sum(-a1))/(2*data_size)
        
    s=0
    min0, min1 = np.min(e_in[0]), np.min(e_in[1])
    if min0<min1:
        s=1
        theta_best=theta[np.argmin(e_in[0])]
    else:
        s=-1
        theta_best=theta[np.argmin(e_in[1])]
    E_in=np.min(np.min(e_in))
    return s,theta_best,E_in
 
def mkDateSet(datPath):
    dataSet = open(datPath, 'r').readlines()
    m = len(dataSet)
    X_train = np.zeros((m, 9))
    Y_train = np.zeros(m)
 
    for i, item in enumerate(dataSet):
        each = item.strip().split()
        X_train[i] = [float(a) for a in each[:-1]]
        Y_train[i] = int(each[-1])
    return (X_train, Y_train)
 
def getData_i(X_train,i):#获取第d维数据
    return np.reshape(X_train[:,i],len(X_train))#从ndarray二维数组转为array一维数组
 
def q19_20():
    (X_train, Y_train)=mkDateSet('hw2_train.dat')
    e_in=np.zeros(9)
    s=np.zeros(9)
    theta=np.zeros(9)
    for i in range(9):
        s[i],theta[i],e_in[i]=deciStump(getData_i(X_train,i),Y_train)
        
    E_in=np.min(e_in)
    dimension=np.argmin(e_in)
    theta_best=theta[dimension]
    s_best=s[dimension]
    
    (X_test, Y_test)=mkDateSet('hw2_test.dat')
    test_len=len(Y_test)
    X_i=getData_i(X_test,dimension)
    q=Y_test*s_best*sign(X_i-theta_best)
    E_out=(test_len-np.sum(q))/(2*test_len)
    print(E_in,E_out)
    
if __name__=='__main__':
    q17_18()#0.16737 0.257180978031
    q19_20()#0.25 0.355
    
    

--------------------- 
作者：海绵酱 
来源：CSDN 
原文：https://blog.csdn.net/zyghs/article/details/78755242 
版权声明：本文为博主原创文章，转载请附上博文链接！