salary=int(input("Enter the salary: "))
late=int(input("Enter the number of late days: "))
absent=int(input("Enter the number of absent days: "))
deduction=0
if late>10 and late<10:
    deduction += 0.10
elif late>5:
    deduction += 0.05
if absent>=2:
    deduction += 0.05
    final_salary=salary-(salary*deduction)
print("Final salary: ",final_salary)
