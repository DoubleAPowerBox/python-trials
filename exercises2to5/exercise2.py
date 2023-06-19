print("Pay Calculator 1.0 - Get What You're Worth!")

#Get hours and rate
hours = input("Enter the amount of hours of work done: ")
rate = input("Enter the pay rate: ")

#Convert hours and rate from str to float variables 
grossPay = float(hours) * float(rate)
print("Your pay is:", grossPay)
