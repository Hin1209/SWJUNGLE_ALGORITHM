import sys

input = sys.stdin.readline

n = int(input())

res = 0

for i in range(1, n+1):
    digits = []
    num = i
    while num > 0:
        digits.append(num % 10)
        num //= 10
    if len(digits) == 2 or len(digits) == 1:
        res += 1
    else:
        diff = digits[0] - digits[1]
        isHan = True
        for j in range(1, len(digits)-1):
            if digits[j] - digits[j+1] != diff:
                isHan = False
                break
            else:
                continue
        if isHan:
            res += 1
print(res)