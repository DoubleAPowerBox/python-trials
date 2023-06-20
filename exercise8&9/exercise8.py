fileHandler = open("mbox-short.txt") #Open file
for line in fileHandler: #Go through each line
  line = line.rstrip() #Remove \n that print adds in
  print(line.upper())