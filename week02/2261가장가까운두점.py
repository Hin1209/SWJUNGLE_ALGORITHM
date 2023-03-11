import sys

input = sys.stdin.readline

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    
points.sort()

def brute_force(start, end):
    min_dist = int(1e10)
    for i in range(start, end-1):
        for j in range(i+1, end):
            dist = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
            min_dist = min(min_dist, dist)
    return min_dist

def divide_conquer(start, end):
    size = end - start
    if size < 3:
        return brute_force(start, end)
    
    mid = (start + end) // 2
    
    left = divide_conquer(start, mid)
    right = divide_conquer(mid, end)
    
    check_point = []
    min_dist = min(left, right)
    
    divide_x = points[mid][0]
    for i in range(start, end):
        if (points[i][0] - divide_x)**2 <= min_dist:
            check_point.append(points[i])
    check_point.sort(key=lambda x:x[1])
    
    
    for i in range(len(check_point)):
        now = check_point[i]
        for j in range(i+1, len(check_point)):
            compare = check_point[j]
            if (compare[1] - now[1])**2 >= min_dist:
                break
            dist = (now[0] - compare[0])**2 + (now[1] - compare[1])**2
            min_dist = min(min_dist, dist)
    
    return min_dist 

print(divide_conquer(0, n))