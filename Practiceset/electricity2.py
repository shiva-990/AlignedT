units=int(input("Enter the number of units: "))
total=0
if units<=100:
    total=units*3
elif units<=200:
    total=100*3+(units-100)*5
else:    total=100*3+100*5+(units-200)*8
print("Total electricity bill: ",total)
