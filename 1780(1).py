paper = []

white = 0
black = 0
blue = 0

def Paper(x, y, N):
    global paper, white, blue, black
    next_N = N // 3

    if N == 1:
        return paper[x][y]

    values = []
    for px, py in ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)) :
        value = Paper(x + px * next_N, y + py * next_N, next_N)
        values.append(value)

    if len(set(values)) == 1:
        return values[0]

    else:
        for value in values:
            if value == -1:
                white += 1
            
            elif value == 0:
                blue += 1
            
            elif value == 1:
                black += 1

        return 2
        
n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

value = Paper(0, 0, n)

if value == -1:
    white += 1

elif value == 0:
    blue += 1

elif value == 1:
    black += 1

print(white) #-1
print(blue) #0
print(black) #1