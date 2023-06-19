numVal = 0
numTotal = 0
numCount = 0
while numVal != "done":
  numVal = input("Enter a number: ")
  try:
    floatNum = float(numVal)
    numTotal += floatNum
    numCount += 1
  except:
    if numVal != "done":
      print("Invalid input, try again.")
numAverage = floatNum / numCount
print("The total is", numTotal, ", the count is", numCount, ", and the average of the inputs is", numAverage)