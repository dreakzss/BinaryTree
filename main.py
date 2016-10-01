class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def treeDepth(tree):
    if tree == None:
        return 0
    leftDepth = treeDepth(tree.left)
    rightDepth = treeDepth(tree.right)
    if leftDepth > rightDepth:
        return leftDepth+1
    if rightDepth >= leftDepth:
        return rightDepth+1

if __name__=='__main__':
    root=Node('D', Node('B', Node('A'), Node('C')), Node('E', right = Node('G', Node('F'))))
    depth=treeDepth(root)
    print('depth:', depth)