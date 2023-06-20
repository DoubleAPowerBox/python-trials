fileName = input("Enter the file name:") # Get the file name
if len(fileName) < 1: fileName = "clown.txt" # Automatically use clown.txt if no input
fileHandler = open(fileName)

wordDict = {} # Create an empty dictionary
for line in fileHandler:
  line = line.rstrip()
  words = line.split()
  for word in words:
    # Return value of item with specified key
    # If a word is not in the dictionary, create an entry and add 1
    # Else just get the value of the word and add 1
    wordDict[word] = wordDict.get(word, 0) + 1

largestCount = 0
largestWord = None
for wordEntry, count in wordDict.items(): # Get both the word and the count from each entry
  print(wordEntry, count)
  if count > largestCount: # Replace previous count with larger count if found
    largestCount = count
    largestWord = wordEntry
    
print(largestWord, "is the most used, with a count of", largestCount)