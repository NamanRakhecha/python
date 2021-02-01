from array import *

arr=array('i',[])
n=int(input())

for i in range(0,n):
    x=int(input())
    n=str(x)
    if(len(n)==10):
        while (x >= 10): 
            x //= 10
        if x in range(7,10): 
            print("YES")
        else:
            print("NO")
    else:
        print("NO")