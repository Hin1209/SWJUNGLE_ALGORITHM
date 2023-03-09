import sys

input = sys.stdin.readline

n = int(input())
number = []
for i in range(n):
    number.append(int(input()))
number.sort()
for i in range(n):
    print(number[i])