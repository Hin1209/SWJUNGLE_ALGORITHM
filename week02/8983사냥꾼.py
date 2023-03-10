import sys

input = sys.stdin.readline

m, n, l = map(int, input().split())
shooting = list(map(int, input().split()))

animals = []
for _ in range(n):
    x, y = map(int, input().split())
    animals.append((x, y))
    
shooting.sort()

cnt = 0

def is_hunted(x, y):
    start = 0
    end = m-1
    if y > l: return False
    distance_hunted = l - y
    while start <= end:
        mid = (start + end) // 2
        if abs(x - shooting[mid]) <= distance_hunted:
            return True
        elif x > shooting[mid]:
            start = mid+1
        elif x < shooting[mid]:
            end = mid-1
    return False

for animal in animals:
    if is_hunted(animal[0], animal[1]):
        cnt += 1
        
print(cnt)