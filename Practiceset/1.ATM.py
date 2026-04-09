balance = int(input("Enter initial account balance: "))
n = int(input("Enter number of transactions: "))

for _ in range(n):
    amount = int(input("Enter withdrawal amount: "))

    if amount % 100 == 0 and balance >= amount:
        print("SUCCESS")
        balance -= amount
    else:
        print("FAILED")

print("Final Balance:", balance)