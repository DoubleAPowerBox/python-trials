numTotal = 0
numCount = 0
while True:
  numVal = input("Enter a number: ")
  if numVal == "done":
    break #Break out of while loop
  try:
    floatNum = float(numVal)
  except:
    print("Invalid input, try again.")
    continue #Stop run of loop and start new run
  #Calculations won't run if continue is called
  numTotal += floatNum
  numCount += 1
  
numAverage = floatNum / numCount
print("The total is", numTotal, ", the count is", numCount, ", and the average of the inputs is", numAverage)