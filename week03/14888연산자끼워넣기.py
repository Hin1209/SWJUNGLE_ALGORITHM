import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

operator = list(map(int, input().split()))

deq = deque()

deq.append((nums[0], 1, operator[0], operator[1], operator[2], operator[3]))

max_num = -int(1e10)
min_num = int(1e10)
while deq:
    num, idx, plus, minus, mul, div = deq.popleft()
    if idx == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        continue
    if plus > 0:
        tmp = num + nums[idx]
        deq.append((tmp, idx+1, plus-1, minus, mul, div))
    if minus > 0:
        tmp = num - nums[idx]
        deq.append((tmp, idx+1, plus, minus-1, mul, div))
    if mul > 0:
        tmp = num * nums[idx]
        deq.append((tmp, idx+1, plus, minus, mul-1, div))
    if div > 0:
        if num < 0:
            tmp = -num // nums[idx]
            tmp *= -1
        else:
            tmp = num // nums[idx]
        deq.append((tmp, idx+1, plus, minus, mul, div-1))

print(max_num)
print(min_num)