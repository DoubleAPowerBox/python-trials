fileHandler = open("mbox-short.txt") #Open file
for line in fileHandler: #Go through each line
  if line.startswith("From "): #Search for lines that start with "From "
    linePieces = line.split() #Split line by whitespace
    print(linePieces[2]) #Print third word in line