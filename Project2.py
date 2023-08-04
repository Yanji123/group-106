from time import time
from pysmx.SM3 import SM3
from string import digits,ascii_lowercase
import random

lib=digits+ascii_lowercase[:6]
print(lib)

res=dict()
length=8
strlen=length//4
print("length=",length)
def randomstring(length):
    return ''.join([random.choice(lib) for _ in range(length)])

def FindCollision():
    sm3 = SM3()
    string=randomstring(64)
    while True:
        sm3.update(string)
        h=sm3.hexdigest()
        h=h[:strlen]
        if h in res:
            t2=time()
            print('Success')
            print([string,res[h][0]],'hashvalue:',h)
            print(t2-t1)
            break
        res[h]=[string,h]
        string=h

t1=time()
FindCollision()
