from array import *

arr=array('I',[])
#n=int(input())

for i in range(0,2):
    x=input()
    if x[0] == "7" or x[0] == "8" or x[0] == "9": 
        print(x[0])
        print("YES")
    else:
        print(x[0])
        print("NO")