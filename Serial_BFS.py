from collections import defaultdict
from collections import deque
import multiprocessing as mp

import multiprocessing


graph = defaultdict(list)
q = deque()


def addEdge(u, v):    
    graph[u].append(v)   
    graph[v].append(u)


def bfs(source):    
    q = deque([source])   
    visited = [0] * numberOfVertices
    distance[source] = 0
    while q:
        front = q.popleft()
        for node in graph[front]:
            if not visited[node]:
                visited[node] = 1
                distance[node] = distance[front] + 1
                q.append(node)
    
        

if __name__ == '__main__':
    
    numberOfVertices, numberOfEdges = map(int, input().split())
    
    
    distance = [0] * numberOfVertices
    for _ in range(numberOfEdges):
        x, y  = map(int, input().split())
        addEdge(x, y)
    
    bfs(0)
    distance[0] = 0
    for i in range(numberOfVertices):
        print( f"Shortest distance of node {i} from source is {distance[i]}")
   


