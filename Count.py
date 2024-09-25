file = open("text.txt")

words = 0

for line in file:
    words += len(line.split())

print("Слов:", words)
