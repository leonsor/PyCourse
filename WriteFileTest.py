# Run this prior to starting the exercise
'''from random import randint as rnd

memReg = 'data/members.txt'
exReg = 'data/inactive.txt'
fee = ('yes', 'no')


def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


genFiles(memReg, exReg) '''''


#  TODO start here with inserting code......


def cleanFiles(currentMem, exMem):
    '''
    currentMem: File containing list of current members
    exMem: File containing list of old members

    Removes all rows from currentMem containing 'no' and appends them to exMem
    '''
    print("start new code")
    exMembers = []
    with open(currentMem, 'r') as readCurrentMem:
        #        with open('membersNew.txt', 'r') as writeCurrentMem:
        currentMembers = readCurrentMem.readlines()
        x = len(currentMembers)
        y = 1
        for member in currentMembers:
            print(member)
            y = y + 1
            if 'no' in member:
                print('inactive member deleted from list and appended to new list')
                exMembers.append(member)
                currentMembers.remove(member)
            print('active member: ' + member)
        print(f'end of loop, checked {y} lines out of {x}')
        print(len(currentMembers))
        print(currentMembers)
        print(len(exMembers))
        print(exMembers)
        #  pass
    print("end new code")


# Code to help you see the files
# Leave as is
memReg = 'data/members.txt'
exReg = 'data/inactive.txt'
cleanFiles(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())


#  TODO End of methods to create

def testMsg(passed):
    if passed:
        return 'Test Passed'
    else:
        return 'Test Failed'


testWrite = "testWrite.txt"
testAppend = "testAppend.txt"
passed = True

#  genFiles(testWrite, testAppend)  #  TODO temporary disabled

with open(testWrite, 'r') as file:
    ogWrite = file.readlines()

with open(testAppend, 'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite, testAppend)
except:
    print('Error')

with open(testWrite, 'r') as file:
    clWrite = file.readlines()

with open(testAppend, 'r') as file:
    clAppend = file.readlines()

# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False

for line in clWrite:
    if 'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print("{}".format(testMsg(passed)))
