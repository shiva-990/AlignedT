drain=int(input("Enter the drain: "))
battery=100
minutes=0

while battery>0:
    battery-=drain
    minutes+=1
print("Minutes until battery is drained: ",minutes)