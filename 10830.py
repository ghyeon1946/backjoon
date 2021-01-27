def power(exp):
    global n, matrix

    matrix_ = [[0 for _ in range(n)] for _ in range(n)]

    if exp == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000

        return matrix

    if exp % 2 == 0:
        a = power(exp // 2)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix_[i][j] += a[i][k] * a[k][j]
        
        for i in range(n):
            for j in range(n):
                matrix_[i][j] %= 1000

        return matrix_

    elif exp % 2 == 1:
        a = power(exp-1)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix_[i][j] += a[i][k] * matrix[k][j]

        for i in range(n):
            for j in range(n):
                matrix_[i][j] %= 1000

        return matrix_

n, exp = input().split()
n, exp = int(n), int(exp)

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        print(power(exp)[i][j])