from concurrent.futures import ThreadPoolExecutor
from time import time
from pysmx.SM3 import SM3
from itertools import product
from string import printable
import random

lib=printable[:-6]
print(lib)

res=dict()
length=48
strlen=length//4
print("length=",length)
def FindCollision():
    sm3 = SM3()
    while True:
        string=''.join(random.sample(lib,20))
        sm3.update(string)
        h=sm3.hexdigest()
        h=h[:strlen]
        if h in res:
            t2=time()
            print('Success')
            print([res[h],string],'hashvalue:',h)
            print(t2-t1)
            break
        res[h]=string

t1=time()
FindCollision()
    
