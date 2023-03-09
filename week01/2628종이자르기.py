import sys

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
row = []
column = []
for _ in range(n):
    isVertical, line = map(int, input().split())
    if isVertical:
        column.append(line)
    else:
        row.append(line)

column.sort()
row.sort()

max_row = max(row[0], h-row[-1]) if len(row) else h
max_col = max(column[0], w-column[-1]) if len(column) else w

for i in range(len(row)-1):
    if row[i+1] - row[i] > max_row:
        max_row = row[i+1] - row[i]
    
for i in range(len(column)-1):
    if column[i+1] - column[i] > max_col:
        max_col = column[i+1] - column[i]
        
print(max_col * max_row)
    