


numDays=int(input("How Many Day's Temperature ?:"))
total=0
temp=[]
for i in range(numDays):
    nextDay=int(input("Enter the temperature for day "+str(i+1)+": "))
    temp.append(nextDay)
    total+=temp[i]
avg=round(total/numDays,2   )
print("\n The average temperature is: "+str(avg))
above=0
for i in temp:
    if i >avg:
        above+=1
print("\n The number of days above the average is: "+str(above))