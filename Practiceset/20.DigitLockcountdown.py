num = int(input("Enter number "))

while num >= 10:   
    temp = num
    digitsum = 0
    while temp > 0:
        digitsum+= temp % 10
        temp //= 10

    num-= digitsum

print("Final digit", num)