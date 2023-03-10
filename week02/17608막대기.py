import sys

input = sys.stdin.readline

n = int(input())

sticks = []
length = 0
for _ in range(n):
    height = int(input())
    if length == 0:
        sticks.append(height)
        length += 1
    else:
        while length > 0 and sticks[-1] <= height:
            sticks.pop()
            length -= 1
        sticks.append(height)
        length += 1

print(length)