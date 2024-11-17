import heapq

pq = [3, 1, 4, 1, 5]
heapq.heapify(pq)

heapq.heappush(pq, -3)
heapq.heappush(pq, -1)
heapq.heappush(pq, -4)
heapq.heappush(pq, -2)

last_value = pq.pop()

print("末尾の要素:", last_value)
print("取り出した後のキュー:", pq)
