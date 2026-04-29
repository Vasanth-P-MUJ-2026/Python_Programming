# Method-1
# for the user input & Type casting
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

#  Compute gross pay
gross_pay = hours * rate

#display the result
print("Pay:", gross_pay)

# Method-2
xh = input("Enter hour: ")
xr = input("Enter rate: ")
xp = float(xh) * float(xr)
print("Pay:", xp)
