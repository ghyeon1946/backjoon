N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

triangle[1][0] = triangle[0][0] + triangle[1][0]
triangle[1][1] = triangle[0][0] + triangle[1][1]

for i in range(2, N):
    triangle[i][0] = triangle[i-1][0] + triangle[i][0]
    for j in range(1, i+1) :
        if j == i:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]

print(max(triangle[N-1]))