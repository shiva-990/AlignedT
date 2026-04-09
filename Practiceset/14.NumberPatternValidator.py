num=input("Enter a digit: ")
is_valid=True
for i in range(len(num)-1):
    if num[i] < num[i+1]:
        is_valid=False
        break

if is_valid:  
    print("YES")
else:
    print("NO")

    