amount=int(input("Enter the amount: "))
deduction=0
if amount>=5000:
    deduction=amount*0.20
elif amount>=3000:
    deduction=amount*0.10
elif amount>=1000:
    deduction=amount*0.05
final_amount=amount-deduction
print("Final amount ",final_amount)
