import re

with open("input.txt", "r") as f:
    s = f.read()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", s)
    answer = 0
    for match in matches:
        a, b = map(int, match.replace("mul(", "").replace(")", "").split(","))
        answer += a * b
    print(answer)