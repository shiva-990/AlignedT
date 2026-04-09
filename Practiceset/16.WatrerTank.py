n=int(input("Enter no of minutes:"))
flow=list(map(int,input("Enter flow :").split()))
capacity=1000
total=0
for i in range(n):
    total+=flow[i]
    if total>capacity:
        print("Overflow",i+1)
        break