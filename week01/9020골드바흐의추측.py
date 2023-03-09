import sys

input = sys.stdin.readline

prime = [True] * (10001)

for i in range(2, 10001):
    if prime[i]:
        n = i * 2
        while n <= 10000:
            prime[n] = False
            n += i

t = int(input())

for _ in range(t):
    num = int(input())
    res = 0
    i = 2
    while i <= num // 2:
        if prime[i] == True and prime[num-i] == True:
            res = i
        i += 1
    print(res, num-res)