from queue import Queue

def bfs(G, s):
    que = Queue()

    dist = [-1]*len(G)

    que.put(s)
    dist[s] = 0

    while not que.empty():
        v = que.get()

        for v2 in G[v]:
            if dist[v2] != -1:
                continue

            que.put(v2)

            dist[v2] = dist[v] + 1
    
    return dist