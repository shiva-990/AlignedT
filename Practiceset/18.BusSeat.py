n = int(input("number of requests: "))
seats = 40
for i in range(n):
    req = int(input("seats requested: "))

    if req <= seats:
        print("CONFIRMED")
        seats -= req
    else:
        print("WAITLISTED")