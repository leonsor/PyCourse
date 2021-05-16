
with open("data/Test1.txt", "w") as File1:
    File1.write('Test 1\n')
    print("File geschreven")

with open("data/Test1.txt", "r") as File2:
    textLines = File2.readlines()
    for line in textLines:
        print(line)
    print("File geopend en geprint")
