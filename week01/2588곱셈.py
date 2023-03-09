import sys

input = sys.stdin.readline

n1 = int(input())
n2 = int(input())

digits = []
while n2 > 0:
    digits.append(n2 % 10)
    n2 //= 10

result = 0
for i, digit in enumerate(digits):
    print(n1 * digit)
    result += n1 * (10**i) * digit 

print(result)