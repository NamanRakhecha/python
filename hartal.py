daysInTotal=int(input("total no of days the calculation have to be done"))
noOfParties=int(input("no of parties that will conduct hartals"))
startDays=[]
totaldays=[]
cannot = []
inter = []

for i in range(0,noOfParties):
    x=int(input("starting days of the hartal"))
    startDays.append(x)

for i in startDays:
    n=i
    while n<=daysInTotal:
        totaldays.append(n)
        n=n+i

#print(totaldays)

for q in range(6,daysInTotal,7):
    cannot.append(q)
for w in range(7,daysInTotal+1,7):
    cannot.append(w)
#print(cannot)

inter = set(totaldays) - set(cannot)

#print(inter)

length=len(inter)
print(length)