temperature=float(input("Enter temperature: "))
unit=input("Enter unit(c/f): ")
if unit == "c":
    f=(temperature*9/5)+32
    print("Temperature in Farenheit: ",f)
elif unit == "f":
    c=(temperature -32)*5/9
    print("Temperature in Celsius: ",c)
else:
    print("Invalid Unit.")
