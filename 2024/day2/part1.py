
reports = []
with open("input.txt", "r") as f:
    for line in f:
        reports.append(list(map(int, line.split())))

answer = 0

for report in reports:
    d = report[0] - report[1]
    safe = True
    if d == 0:
        continue
    elif d > 0:
        # ascending
        for i in range(len(report) - 1):
            dif = report[i] - report[i + 1]
            if dif < 1 or dif > 3:
                safe = False
                break
        if safe:
            answer += 1           
    else:
        # descending
        for i in range(len(report) - 1):
            dif = report[i] - report[i + 1]
            if dif < -3 or dif > -1:
                safe = False
                break
        if safe:
            answer += 1           

print(answer) 


