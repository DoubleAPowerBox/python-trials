#Extract portion after colon and turn it into a float
str = 'X-DSPAM-Confidence: 0.8475'
print(str)
for i in str:
  if i.isdigit() == False:
    #print(i)
    if i == ".":
      continue
    str = str.strip(i)
floatStr = float(str)
print(floatStr)
print(floatStr + 1.0) #Test if float