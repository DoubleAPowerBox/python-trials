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

wordTupleList = []
for wordEntry, count in wordDict.items(): # Get both the word and the count from each entry
  wordTuple = (count, wordEntry) # Make a tuple for each entry; value first, word second
  wordTupleList.append(wordTuple) # Add the tuple to a list of tuples
wordTupleList = sorted(wordTupleList, reverse=True) # Sort from largest value to smallest by key (reverse=True)
print(wordTupleList[:5]) # Print out the 5 most used words

# This single statement does the SAME THING! WOAH.
print(sorted([(c, wE) for wE, c in wordDict.items()], reverse=True)[:5])