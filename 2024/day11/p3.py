def getDigits(num):
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1
    return digits

def ans(stone, blinks):
    if blinks == 0:
        return 1
    if (stone, blinks) not in cache:
        if stone == 0:
            return ans(1, blinks - 1)
        digits = getDigits(stone)
        if digits % 2 == 0:
            left = stone // 10 ** (digits // 2)
            right = stone % 10 ** (digits // 2)

            a = ans(left, blinks - 1)
            cache[(left, blinks - 1)] = a
            b = ans(right, blinks - 1)
            cache[(right, blinks - 1)] = b
            result = a + b
        else:
            result = ans(stone * 2024, blinks - 1)
        cache[(stone, blinks)] = result
    return cache[(stone, blinks)]

cache = {}
with open("input.txt", "r") as f:
    data = list(map(int, f.read().strip().split(" ")))

print(data)
out = 0
for stone in data:
    out += ans(stone, 1000)
print(out)
