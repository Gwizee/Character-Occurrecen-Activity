text = input("Enter a word: ")
char = input("Enter the character you want to see: ")

i = 0
count = 0

while i < len(text) :
    letter = text[i]
    if letter == char :
        count += 1
    i += 1
print(count)