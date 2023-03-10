import sys

input = sys.stdin.readline

n = int(input())

liquid = list(map(int, input().split()))
liquid.sort()

def make_neutral(start, end, target):
    min_value = [int(1e10), 0]
    while start <= end:
        mid = (start + end) // 2
        composite = liquid[target] + liquid[mid]
        if composite == 0:
            return [0,mid]
        elif composite > 0:
            if min_value[0] > abs(composite):
                min_value[0] = abs(composite)
                min_value[1] = mid
            end = mid-1
        else:
            if min_value[0] > abs(composite):
                min_value[0] = abs(composite)
                min_value[1] = mid
            start = mid+1
    return min_value

min_liquid = int(1e10)
min_idx = -1
for i in range(n):
    res = make_neutral(i+1, n-1, i)
    if res[0] < min_liquid:
        min_liquid = res[0]
        min_idx = (i, res[1])
        
print(liquid[min_idx[0]], liquid[min_idx[1]])
        