import sys

input = sys.stdin.readline

N = int(input())

word = []

for i in range(N):
    tmp = input().rstrip()
    word.append((len(tmp), tmp))
tmp_set = set(word)
word = list(tmp_set)
word.sort()

for i in range(len(word)):
    print(word[i][1])