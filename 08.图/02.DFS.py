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
    path = {start:None}
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for m in nodes:
            if m not in seen:
                stack.append(m)
                seen.add(m)
                path[m] = vertex
        # print(vertex)
    return path

path = DFS(graph,"A")

""" 看A到F的路径 """
v = "F"
while v != None:
    print(v)
    v = path[v]