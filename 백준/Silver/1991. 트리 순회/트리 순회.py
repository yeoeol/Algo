n = int(input())
tree = dict()

for _ in range(n):
    middle, left, right = input().split()
    tree[middle] = list()
    tree[middle].append(left)
    tree[middle].append(right)

def preorder(parent):
    print(parent, end='')
    left, right = tree.get(parent)
    if left == '.' and right == '.':
        return
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

def inorder(parent):
    left, right = tree.get(parent)
    if left == '.' and right == '.':
        print(parent, end='')
        return
    if left != '.':
        inorder(left)
    print(parent, end='')
    if right != '.':
        inorder(right)

def post(parent):
    left, right = tree.get(parent)
    if left == '.' and right == '.':
        print(parent, end='')
        return
    if left != '.':
        post(left)
    if right != '.':
        post(right)
    print(parent, end='')

preorder('A')
print()
inorder('A')
print()
post('A')