paper = []

white = 0
black = 0
blue = 0

def Paper(x, y, N):
    global paper, white, black, blue
    next_N = N // 3

    if N == 1:
        return paper[x][y]

    a = Paper(x, y, next_N)
    b = Paper(x + next_N, y, next_N)
    c = Paper(x + 2 * next_N, y, next_N)

    d = Paper(x, y + next_N, next_N)
    e = Paper(x + next_N, y + next_N, next_N)
    f = Paper(x + 2 * next_N, y + next_N, next_N)

    g = Paper(x, y + 2 * next_N, next_N)
    h = Paper(x + next_N, y + 2 * next_N, next_N)
    i = Paper(x + 2 * next_N, y + 2 * next_N, next_N)

    if a == b == c == d == e == f == g == h == i == -1:
        return -1

    elif a == b == c == d == e == f == g == h == i == 1:
        return 1

    elif a == b == c == d == e == f == g == h == i == 0:
        return 0

    else:
        if a == -1 :
            white += 1
        elif a == 1 :
            black += 1
        elif a == 0:
            blue += 1
 
        if b == -1 :
            white += 1
        elif b == 1 :
            black += 1
        elif b == 0:
            blue += 1

        if c == -1 :
            white += 1
        elif c == 1 :
            black += 1
        elif c == 0:
            blue += 1

        if d == -1 :
            white += 1
        elif d == 1 :
            black += 1
        elif d == 0:
            blue += 1

        if e == -1 :
            white += 1
        elif e == 1 :
            black += 1
        elif e == 0:
            blue += 1

        if f == -1 :
            white += 1
        elif f == 1 :
            black += 1
        elif f == 0:
            blue += 1

        if g == -1 :
            white += 1
        elif g == 1 :
            black += 1
        elif g == 0:
            blue += 1

        if h == -1 :
            white += 1
        elif h == 1 :
            black += 1
        elif h == 0:
            blue += 1

        if i == -1 :
            white += 1
        elif i == 1 :
            black += 1
        elif i == 0:
            blue += 1

    return 2
    
def Answer(x, y, N):
    global white, black, blue
    
    if not Paper(x, y, N) == 2:
        if Paper(x, y, N) == -1:
            white += 1

        elif Paper(x, y, N) == 0:
            blue += 1

        elif Paper(x, y, N) == 1:
            black += 1

        
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

Answer(0, 0, n)

print(white) #-1
print(blue) #0
print(black) #1