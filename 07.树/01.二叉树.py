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

print(e.lchild.rchild.data) # C