class student:

    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2

    def average(self):
        return (self.m1 + self.m2)/2

    def show(self):
        print(self.name , self.rollno)
        avg=self.average()
        print(avg)
    

s1=student('naman',43,43,57)
s1.show()
print(s1.average())