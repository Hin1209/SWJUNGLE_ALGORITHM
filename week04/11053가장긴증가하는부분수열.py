import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [nums[0]]

for i in range(1, n):
    if dp[-1] > nums[i]:
        idx = bisect_left(dp, nums[i])
        dp[idx] = nums[i]
    elif dp[-1] < nums[i]:
        dp.append(nums[i])
print(len(dp))