import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
day_rise = A - B
if (V - A) % day_rise == 0:
    print((V - A) // day_rise + 1)
else:
    print((V - A) // day_rise + 2)