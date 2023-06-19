#Extract portion after colon and turn it into a float
str = 'X-DSPAM-Confidence: 0.8475'
print(str)

findColonPos = str.find(":")
print(findColonPos)
#Using : will include the char at that index num and all chars after it
#It's like bit allcation notation
strPiece = str[findColonPos + 2:]
print(strPiece)
floatStr = float(strPiece)
print(floatStr)
print(floatStr + 1.0) #Test if float