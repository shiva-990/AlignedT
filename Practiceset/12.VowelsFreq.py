sent=str(input("Enter a string: "))
vowels="aeiouAEIOU"
cnt=0
for i in sent:
    if i in vowels:
        cnt+=1  
print("Number of vowels in the string: ",cnt)