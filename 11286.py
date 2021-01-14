import heapq
import sys

n = int(input())

Min_heap = []
for i in range(n):
    item = int(sys.stdin.readline())

    if item != 0:
        heapq.heappush(Min_heap, (abs(item), item))
    
    else:
        if not Min_heap:
            print(0)
        
        else:
            print(heapq.heappop(Min_heap)[1])