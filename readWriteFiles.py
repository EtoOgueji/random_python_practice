import os

# overwrite
with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some randome text\nMore random text\nAnd some more")

# read
with open("mydata.txt", encoding="utf-8") as myFile:

    print(myFile.read())

print(myFile.closed)

print(myFile.name)

os.rename("mydata.txt", "mydata2.txt")

print(myFile.name)

os.remove("mydata2.txt")

os.mkdir("mydir")

os.chdir("mydir")

print("Current Dir: ", os.getcwd())

os.chdir("..")

print("Currenty Directory: ", os.getcwd())

os.rmdir("mydir")
