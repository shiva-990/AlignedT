binary=int(input("Enter a binary number: "))
decimal=0
power=0
for i in reversed(str(binary)):
    decimal+=int(i)*(2**power)
    power+=1
print("Decimal equivalent: ",decimal)