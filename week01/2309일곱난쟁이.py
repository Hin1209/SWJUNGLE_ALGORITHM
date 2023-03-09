import sys
from itertools import combinations

input = sys.stdin.readline

candidates = combinations(range(9), 7)
dwarf = []

for _ in range(9):
    dwarf.append(int(input()))
    
for candidate in candidates:
    sum_dwarf = 0
    seven_dwarf = []
    for idx in candidate:
        sum_dwarf += dwarf[idx]
        seven_dwarf.append(dwarf[idx])
    if sum_dwarf == 100:
        break

seven_dwarf.sort()
for i in seven_dwarf:
    print(i)