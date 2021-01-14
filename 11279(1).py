import heapq
import sys

n = int(input())

Max_heap = []
for i in range(n):
    item = int(sys.stdin.readline())
    
    if item != 0:
        heapq.heappush(Max_heap, (-item, item))
    
    else:
        if not Max_heap:
            print(0)

        else:
            print(heapq.heappop(Max_heap)[1])