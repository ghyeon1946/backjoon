paper = []

white = 0
blue = 0

WHITE = 0
BLUE  = 1
BAD   = 2

def Paper(x, y, N):
    global paper, white, blue
    next_N = N // 2

    if N == 1:
        return paper[x][y]

    values = []
    for px, py in ((0, 0), (1, 0), (0, 1), (1, 1)):
        value = Paper(x + px * next_N, y + py * next_N, next_N)
        values.append(value)

    if len(set(values)) == 1:
        return values[0]

    else:
        for value in values:
            if value == WHITE:
                white += 1

            elif value == BLUE:
                blue += 1

        return BAD

n = int(input())

for i in range(n):
    paper.append(list(map(int, input().split())))

value = Paper(0, 0, n)

if value == WHITE:
    white += 1

elif value == BLUE:
    blue += 1

print(white)
print(blue)