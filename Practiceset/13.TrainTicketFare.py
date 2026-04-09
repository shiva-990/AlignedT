distance=int(input("Enter the distance: "))
age=int(input("Enter the age:"))
fare=distance*2
if age <12:
    bill = fare - (fare*0.5)
elif age >= 60:
    bill = fare - (fare*0.3)
else:
    bill = fare
print("The train ticket fare is: ",bill)