from queue import Queue

def bfs(G, s):
    que = Queue()

    dist = [-1]*len(G)

    que.put(s)
    dist[s] = 0