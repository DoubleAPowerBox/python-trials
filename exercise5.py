def computePay(hours, rate):
  if hours > 40:
    print("Overtime Hours! Well done, slave.")
    overtimePay = (hours - 40.0) * (rate * 0.5)
  else:
    overtimePay = 0;
  grossPay = (hours * rate) + overtimePay
  return grossPay

print("Pay Calculator 4.0 - Now With Included Function!")

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

calculatedPay = computePay(floatHours, floatRate)
print("Your pay is:", calculatedPay)
