__author__ = 'brodyzt'
def removeSymbolsFromList(list):
    tempList = [[],[]]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(len(list[0])):
        if(alphabet.__contains__(list[0][x])):
            tempList[0].append(list[0][x])
            tempList[1].append(list[1][x])
    return tempList
def sortListsByFrequency(list):
    listSorted = False
    while(listSorted == False):
        listSorted = True
        for x in range(0, len(list[0]) - 1):
            if(list[1][x] > list[1][x+1]):
                charTemp = list[0][x+1]
                list[0][x+1] = list[0][x]
                list[0][x] = charTemp
                frequencyTemp = list[1][x+1]
                list[1][x+1] = list[1][x]
                list[1][x] = frequencyTemp

                listSorted = False
    return list

charAndFreq = [[],[]]
userText = raw_input("Please enter some text to analyze: ").lower()

for char in userText:
    if(charAndFreq[0].__contains__(char)):
        charAndFreq[1][charAndFreq[0].index(char)] += 1
    else:
        charAndFreq[0].append(char)
        charAndFreq[1].append(1)

charAndFreq = removeSymbolsFromList(charAndFreq)
charAndFreq = sortListsByFrequency(charAndFreq)

#the following will print the least common characters
print('\nThe least common characters: ')
for x in range(0,len(charAndFreq[0])):
    print(str(charAndFreq[0][x]) + ' appears ' + str(charAndFreq[1][x]) + ' %s in the user inputted string' % ('times','time')[charAndFreq[1][x] == 1])
    if(x == len(charAndFreq[0]) - 1 or charAndFreq[1][x] != charAndFreq[1][x+1]):
        break

#the following will print the most common characters
print('\nThe most common characters are: ')
for x in range(len(charAndFreq[0]) - 1, 0, - 1):
    print(str(charAndFreq[0][x]) + ' appears ' + str(charAndFreq[1][x]) + ' %s in the user inputted string' % ('times','time')[charAndFreq[1][x] == 1])
    if(x == 0 or charAndFreq[1][x] != charAndFreq[1][x-1]):
        break