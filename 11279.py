import heapq
import sys

def Max_Heap(heap_items):
    global n
    
    Max_heap = []
    for i in range(n):
        if heap_items[i] != 0:
            heapq.heappush(Max_heap, (-heap_items[i], heap_items[i]))

        else:
            if not Max_heap:
                print(0)
            
            else:
                print(heapq.heappop(Max_heap)[1])

n = int(input())

heap_items = []
for i in range(n):
    heap_items.append(int(sys.stdin.readline())

Max_Heap(heap_items)