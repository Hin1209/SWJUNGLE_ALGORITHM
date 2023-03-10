import sys

input = sys.stdin.readline

n, m = map(int, input().split())
MAX = int(1e9)
MIN = 0

woods = list(map(int, input().split()))

def find_maximum(start, end, target):
    previous_height = MIN
    while start <= end:
        mid = (start + end) // 2
        wood_taken = 0
        for i in range(n):
            if woods[i] > mid:
                wood_taken += (woods[i] - mid)
        if wood_taken == target:
            return mid
        elif wood_taken > target:
            start = mid+1
            previous_height = max(previous_height, mid)
        elif wood_taken < target:
            end = mid-1
    return previous_height

print(find_maximum(MIN, MAX, m))