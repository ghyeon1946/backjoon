paper = []

white = 0
black = 0

def Paper(x, y, N):
    global paper, white, black
    next_N = N // 2

    if N == 1:
        return paper[x][y]

    a = Paper(x, y, next_N)
    b = Paper(x + next_N, y, next_N)
    c = Paper(x, y + next_N, next_N)
    d = Paper(x + next_N, y + next_N, next_N)

    if a == b == c == d == 1:
        return 1
    elif a == b == c == d == 0:
        return 0
    else:
        if a == 1 :
            white += 1
        elif a == 0:
            black += 1
 
        if b == 1:
            white += 1
        elif b == 0:
            black += 1

        if c == 1:
            white += 1
        elif c == 0:
            black += 1

        if d == 1:
            white += 1
        elif d == 0:
            black += 1
    return 2
    
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

Paper(0, 0, n)

print(black)
print(white)