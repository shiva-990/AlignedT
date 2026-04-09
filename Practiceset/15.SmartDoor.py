pin=int(input("Set your 4 digit pin: "))

n=3

while n>0:
    digit=int(input("Enter a digit: "))
    if digit==pin:
        print("Access granted")
        break
    else:
        print("Access denied")
        n-=1
if n == 0:
    print("Account Locked")