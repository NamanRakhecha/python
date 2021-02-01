def append_bit(x,l):
    return[x + element for element in l]

def generateBit(n):
    if n==0: return[]
    if n==1: return["0","1"]
    else:
        return (append_bit("0",generateBit(n-1)) + append_bit("1",generateBit(n-1)) )


n=int(input("enter size"))
lmt=int(input("enter limit"))
lst=[]

lst=generateBit(n)
for i in lst:
    sum=0
    for x in i:
        z = int(x)
        sum = sum + z
    if sum>lmt:
        print(i)
