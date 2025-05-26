import re

with open("input.txt", "r") as f:
    s = f.read()
    matches = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", s)
    answer = 0
    on = True
    for match in matches:
        if match == "do()":
            on = True
            continue
        elif match == "don't()":
            on = False
            continue
        if on:
            a, b = map(int, match.replace("mul(", "").replace(")", "").split(","))
            answer += a * b
    print(answer)