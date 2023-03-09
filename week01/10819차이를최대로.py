import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

candidates = permutations(nums, n)

max_sum = 0
for candidate in candidates:
    sum = 0
    pre_num = 0
    for i, num in enumerate(candidate):
        if i == 0:
            pre_num = num
            continue
        sum += abs(pre_num - num)
        pre_num = num
    max_sum = max(max_sum, sum)

print(max_sum)