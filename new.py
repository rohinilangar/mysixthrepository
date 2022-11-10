#count no of lines in python file
f = open("sample.txt", "w")
f.write("hello welcome to the sample file!.\n write your data \n and test it.")
f.close()

f = open("sample.txt", "r")
count = 0
for line in f:
    if line != "\n":
        count += 1
        print("no of lines is:",count)
