# 二叉树
class BinearTree(object):
    def __init__(self,item):
        self.data = item
        self.lchild = None
        self.rchild = None

a = BinearTree("A")
b = BinearTree("B")
c = BinearTree("C")
d = BinearTree("D")
e = BinearTree("E")
f = BinearTree("F")
g = BinearTree("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e

def pre_order(root):
    # 前序遍历：先根 -> 左子树 -> 右子树
    if root:
        print(root.data,end=' ')
        pre_order(root.lchild)
        pre_order(root.rchild)
print("树的前序遍历：",end='')
pre_order(root)

print()
def in_order(root):
    # 中序遍历：先左子树 -> 根 -> 右子树
    if root:
        in_order(root.lchild)
        print(root.data,end=' ')
        in_order(root.rchild)
print("树的中序遍历：",end='')
in_order(root)

print()
def back_order(root):
    # 后序遍历：先左子树 -> 右子树 -> 根
    if root:
        back_order(root.lchild)
        back_order(root.rchild)
        print(root.data,end=' ')
print("树的中序遍历：",end='')
back_order(root)