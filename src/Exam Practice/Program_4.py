word = input("Enter a word: ")
if word[-3:] == "ing":
    word = word[:-3] + "ly"
else:
    word += "ing"
print(word)