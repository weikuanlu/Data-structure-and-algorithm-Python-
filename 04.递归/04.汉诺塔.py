# -*- coding = utf-8 -*-
"""
这是动态规划问题中的一种，用递归来实现较为简单方便。
对于"将 n 个圆盘从 A 柱移动到 C 柱（借助 B 柱）"这个问题，我们可以通过以下三步实现：
    将 A 柱最上面的 n-1 个圆盘移动到 C 柱（借助 B 柱）
    将 A 柱上剩下的那 1 个圆盘直接移动到 C 柱
    将 B 柱上的 n-1 个圆盘移动到 C 柱（借助 A 柱）
"""
def hanoi(n,a,b,c):
    if n == 1:
        print(a,"--",c)
        return None
    else:
        hanoi(n-1,a,c,b)
        print(a,"--",c)
        hanoi(n-1,b,a,c)

if __name__ == "__main__":
    numbers = int(input("请输入："))
    hanoi(numbers,"a","b","c")
