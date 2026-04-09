T=int(input("Enter time "))
time=T%60
if time==0:
    time=90

if 1<=time<=30:
    print("RED")
elif 31<=time<=45:
    print("YELLOw")
else:
    print("GREEN")
