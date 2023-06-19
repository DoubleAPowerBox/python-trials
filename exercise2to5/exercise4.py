print("Pay Calculator 3.0 - Now With Invaild Input Detection!")

#Get hours and rate
strHours = input("Enter the amount of hours of work done: ")
strRate = input("Enter the pay rate: ")
try:
#Convert hours and rate from str to float variables
  floatHours = float(strHours)
  floatRate = float(strRate)
except:
  print("Put in a numeric value, dummy!")
  quit() #Abort program
  
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
