# 有向图
import math
import heapq

graph = {
    "V0":{"V2":10,"V4":30,"V5":100},
    "V1":{"V2":5},
    "V2":{"V3":50},
    "V3":{"V5":10},
    "V4":{"V3":20,"V5":60},
    "V5":{"V5":0}
}

def init_distance(graph,s):
    distance = {s:0}
    for key in graph.keys():
        if key != s:
            distance[key] = math.inf

    return distance

def dijkstra(graph,s):
    pqueue = []
    heapq.heappush(pqueue,(0,s))
    seen = set()

    path = {s:None}
    distance = init_distance(graph,s)
    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for m in nodes:
            if m not in seen:
                if dist + graph[vertex][m] < distance[m]:
                    heapq.heappush(pqueue,(dist + graph[vertex][m],m))
                    distance[m] = dist + graph[vertex][m]
                    path[m] = vertex

    return path,distance

path,distance = dijkstra(graph,"V0")
print(path)
print(distance)















