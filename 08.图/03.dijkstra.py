import heapq
import math

"""
狄克斯特拉（Dijkstra）算法也是求解最短路径问题的算法，使用它可以求得从起点到终点的路径中权重总和最小的那条路径路径。
    使用优先队列来实现，优先队列是依据二叉堆实现
"""
# 定义无向图，前面的key是结点，后面的value列表里面：key是与前面结点相邻的结点，value是边的权重
graph = {
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
}

def init_distance(graph,s):
    distance = {s:0}
    for vertex in graph.keys():
        if vertex != s:
            distance[vertex] = math.inf
    return distance

def dijkstra(graph,s):
    pqueue = [] # 定义优先队列 -- 结合下面
    heapq.heappush(pqueue,(0,s))
    seen = set()
    parent = {s:None}
    distance = init_distance(graph,s)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys() # 与vertex 相邻的结点
        for w in nodes:
            if w not in seen: # 如果结点没有弹出
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]
    return parent,distance

parent,distance = dijkstra(graph,"A")
print(parent)
print(distance)
