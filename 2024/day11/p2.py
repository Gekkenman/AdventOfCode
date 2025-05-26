#from math import ceil
#with open("example.txt", "r") as f:
    #data = list(map(int,f.read().strip().split(" ")))

def getDigits(num):
    digits = 1
    while num > 10:
        num = num // 10
        digits += 1
    return digits

def listContainsSingleDigitNum(data):
    out = True
    for num in data:
        if getDigits(num) == 1:
            out = False
    return out
    

def getLookUpNum(num):
    if num == 0:
        return {1:[1]}
    dic = {}
    data = [num]
    i = 1
    while len(data) == 1 or listContainsSingleDigitNum(data):
        temp = []
        for stone in data:
            digits = getDigits(stone)
            if stone == 0:
                temp.append(1)
            elif not digits % 2:
                temp.append(stone // 10 ** (digits // 2))
                temp.append(stone % 10 ** (digits // 2))
            else:
                temp.append(stone * 2024)
        data = temp
        dic[i] = data 
        i += 1
    return dic


def getLookUpTable():
    dic = {x:{} for x in range(10)}
    for key in dic:
        dic[key] = getLookUpNum(key)
    dic[32] = {1: [3, 3]}
    dic[77] = {1: [7, 7]}
    dic[26] = {1: [2, 6]}
    return dic

lookUp = getLookUpTable()

data = [0]


for p in x:
    print(x[p])