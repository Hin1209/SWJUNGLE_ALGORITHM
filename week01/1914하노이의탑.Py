import sys

input = sys.stdin.readline

def hanoi(n, start, end):
    if n > 1:
        hanoi(n-1, start, 6 - start - end)
    print(start, end)
    if n > 1:
        hanoi(n-1, 6 - start - end, end)
        
    
n = int(input())
print(2**n-1)
if n <= 20: hanoi(n, 1, 3)