
def main():
    reports = []
    with open("input.txt", "r") as f:
        for line in f:
            reports.append(list(map(int, line.split())))

    answer = 0

    assert reportIsValid([1, 2, 3, 4, 5]) == True
    assert reportIsValid([1, 1, 3, 4, 5]) == True
    assert reportIsValid([1, 4, 3, 4, 5]) == True
    assert reportIsValid([1, 200, 3, 4, 5]) == True
    assert reportIsValid([5, 2, 3, 4, 5]) == True
    assert reportIsValid([200, 2, 3, 4, 5]) == True
    assert reportIsValid([3, 2, 3, 4, 1]) == False
    
    for report in reports:
        if reportIsValid(report):
            answer += 1
    print(answer)

def reportIsValid(report):
    bad = getSusIndex(report)
    safe = True
    if 0 < len(bad) < 4:
        for i in bad:
            temp = report.copy()
            temp.pop(i)
            if len(getSusIndex(temp)) == 0:
                return True
            else:
                safe = False
    elif len(bad) > 3:
        safe = False
    return safe    

def getSusIndex(report):
    bad = set()
    if isAcending(report):
        for i in range(len(report) - 1):
            dif = report[i] - report[i + 1]
            if dif < -3 or dif > -1:
                bad.add(i)
                bad.add(i + 1)
    else:
        for i in range(len(report) - 1):
            dif = report[i] - report[i + 1]
            if dif < 1 or dif > 3:
                bad.add(i)
                bad.add(i + 1)
    return bad

def isAcending(report):
    result = 0
    for i in range(3):
        d = report[i] - report[i + 1]
        if d > 0:
            result += 1
        elif d < 0:
            result -= 1
    if result > 0:
        return False
    else:
        return True
    
if __name__ == "__main__":
    main()

    

