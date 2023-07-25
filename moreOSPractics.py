import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("line", lineNum)

        wordList = line.split()

        print("Number of words", len(line))

        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        avgNumChars = charCount / len(wordList)

        print("Avg word Length: {:.2}".format(avgNumChars))

        lineNum += 1