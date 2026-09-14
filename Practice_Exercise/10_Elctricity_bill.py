units=float(input("Enter Electricity Units Consumed: "))
if units<=100:
    bill=(units*5)
elif units<=200:
    bill=(100*5)+((units-100)*7)
elif units<=300:
    bill=(100*5)+(100*7)+((units-200)*10)
else:
    bill=(100*5)+(100*7)+(100*10)+((units-300)*15)
print("Electricity Bill is: ",bill)
  