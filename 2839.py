def Sugar(n):
    cache = [-1, -1, -1, 1, -1, 1]

    for i in range(6, n+1):
        cache.append(1 + cache[i-5])

        if cache[i] == 0:
            cache[i] = -1
        
            if i % 3 == 0:
                cache[i] = i // 3

    return cache[n]

n = int(input())
print(Sugar(n))