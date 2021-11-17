"""
BFS(广度优先搜索)：是一种对图进行搜索的算法。
    借助队列：先进先出的性质实现
    假设我们一开始位于某个顶点（即起点），此时并不知道图的整体结构，而我们的目的是从起点开始顺着边搜索，直到到达指定顶点（即终点）。
    在此过程中每走到一个顶点，就会判断一次它是否为终点。广度优先搜索会优先从离起点近的顶点开始搜索。
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

def BFS(graph,start):
    queue = [] # 创建队列 -- 利用列表的操作 实现一个队列
    queue.append(start)
    seen = set() # 创建集合，避免让元素重复进入队列
    seen.add(start)
    path = {}
    path[start] = None
    while len(queue) > 0:
        key = queue.pop(0)
        b = graph[key]
        for m in b:
            if m not in seen:
                queue.append(m)
                seen.add(m)
                path[m] = key
        print(key)
    return path

path = BFS(graph,"A")
# print(path)
for key,value in path.items():
    print(f"{key}:{value}")