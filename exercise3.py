print("Pay Calculator 2.0 - Now With Better Pay!")

#Get hours and rate
strHours = input("Enter the amount of hours of work done: ")
strRate = input("Enter the pay rate: ")

#Convert hours and rate from str to float variables
floatHours = float(strHours)
floatRate = float(strRate)
#print(floatHours, floatRate)

#Check if hours exceed 40 for overtime pay
#Take excess hours done and multiply by 0.5 times the rate
if floatHours > 40:
  print("Overtime Hours! Well done, slave.")
  overtimePay = (floatHours - 40.0) * (floatRate * 0.5)
else:
  overtimePay = 0;
grossPay = (floatHours * floatRate) + overtimePay
print("Your pay is:", grossPay)