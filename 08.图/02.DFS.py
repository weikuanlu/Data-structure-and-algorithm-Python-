"""
DFS(深度优先搜索)：是一种对图进行搜索的算法。
    借助栈：先进后出的性质实现
    深度优先搜索会沿着一条路径不断往下搜索直到不能再继续为止，然后再折返，开始搜索下一条候补路径。
"""

# 定义一个图
graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

def DFS(graph,start):
    stack = []
    stack.append(start)
    seen = set()
    seen.add(start)

    while len(stack)>0:
        key = stack.pop()
        b = graph[key]
        for m in b:
            if m not in seen:
                stack.append(m)
                seen.add(m)
        print(key)
DFS(graph,"B")