def Add(n):
    cache = []

    cache.append([0, 0])
    cache.append([1, 1])
    cache.append([2, 2])
    cache.append([3, 4])

    for i in range(4,n+1):
        cache.append([i, cache[i-1][1] + cache[i-2][1] + cache[i-3][1]])
    
    print(cache[n][1])

n = int(input())

for i in range(n):
    Add(int(input()))