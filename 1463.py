n = int(input())

cache = [0, 0, 1, 1]

for i in range(4, n+1):
    temp = []
    if i % 3 == 0:temp.append(cache[i//3])
    if i % 2 == 0:temp.append(cache[i//2])
    if i-1 > 0: temp.append(cache[i-1])
    
    Min = min(temp)
    cache.append(Min+1)

print(cache[n])