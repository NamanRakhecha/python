
class sup:
    def pri(self,arr):
        for i in arr:
            print(i)

class sub(sup):
    print("sublass")
    def pri(self,arr):
        print("im in")

s=sub
arr = {1,2,3,1,4,5,2,7}
s.pri(s,arr)