import math
A=int(input("Enter A: "))
B=int(input("Enter B: "))

count=0

for num in range(A,B+1):
    if num>1:
        isprime=True
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                isprime=False
                break
        if isprime:
            count+=1
print("prime count: ",count)            