import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

def multifly(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    half = b // 2
    res = multifly(a, half)
    res = (res * res) % c
    if b % 2 == 1:
        res = (res * a) % c
    return res

print(multifly(a, b))