n = int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
arr.sort(reverse=True)
print(arr)
i=0
while i<n:
    if arr[i]>arr[i+1]:
        print(arr[i+1])
        break
    else:
       i=i+1
