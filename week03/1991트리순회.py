import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = {'left': left, 'right': right}

def preOrder(now):
    print(now, end="")
    if tree[now]['left'] != '.':
        preOrder(tree[now]['left'])
    if tree[now]['right'] != '.':
        preOrder(tree[now]['right'])
    
def inOrder(now):
    if tree[now]['left'] != '.':
        inOrder(tree[now]['left'])
    print(now, end="")
    if tree[now]['right'] != '.':
        inOrder(tree[now]['right']) 
    
def postOrder(now):
    if tree[now]['left'] != '.':
        postOrder(tree[now]['left'])
    if tree[now]['right'] != '.':
        postOrder(tree[now]['right'])
    print(now, end="")

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')