import math


def leibnizPi(n):
    pi=0.0
    for i in range(0,n):
        pi+=((-1.0)**i)/(2*i+1)
    pi*=4
    return pi 
# 5zn8ku?

def nilakanthaPi(n):
    pi =0.0
    for i in range(0,n-1):
        pi+=((-1.0)**i)*4/((2+i*2)*(3+i*2)*(4+i*2))
    return pi+3.0


def newtonPi(x0):
    cnt=0
    x_new = x0
    while True:
        x_old = x_new
        x_new = x_new - (math.sin(x_new))/(math.cos(x_new))
        if(abs(x_new-x_old)<1e-10):
            return x_new
        cnt += 1
