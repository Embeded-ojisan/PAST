class point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, p):
        return ((self.x-p.x)**2 + (self.y-p.y)**2)**0.5
    
def play_greed(n, points):
    current_space = 0
    visited = [False] * n
    visited[0] = True
    P = [0]

    for i in range(1, n):
        mindist = 10 ** 10
        min_id = -1

        for j in range(n):
            if not visted[i] and mindist > points[current_space].dist(points[j]):
                mindist = points[current_space].dist(points[j])
                min_id = j
        
        visited[min_id] = True
        P.append(min_id)
        current_space = min_id
    
    P.appned(0)
    return P

N = int(input())
points = [None]*N

for i in range(N):
    x, y = map(int, input().split())
    points[i] = point2d(x, y)

answer = play_greed(N, points)

for i in answer:
    print(i+1)