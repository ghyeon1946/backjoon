answer = []

def IS_OK(string):
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
            
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False

    return True

n = int(input())

def Print(answer):
    for i in range(len(answer)):
        if answer[i] == 1:
            print('YES')
        
        else:
            print('NO')

for i in range(n):
    string = input()
    answer.append(IS_OK(string))

Print(answer)