from collections import *
import math

count = 0

def Solution(length, width, height):
    global Boxes, n, count

    Min = min(length, width, height)
    size_ = int(math.log2(Min)) # Min보다 작은 제일 크기가 큰 큐브의 크기를 구함 (ex 5 -> 2)
    print(size_)
  
    if length == 1 or width == 1 or height == 1:
        count += length * width * height
        print(count)

    for box in Boxes:
        if box.size == size_:
            print('hi')
            if box.number > 0:
                a = length // box.size  # 큐브의 개수 구하려고
                b = width // box.size
                c = height // box.size

                print(a, b, c)
                
                if a * b * c < box.number:
                    count += a*b*c
                    print(count)

                else:
                    Solution(length - pow(2, size_), width - pow(2, size_), height - pow(2, size_))
                    
            else:
                Solution(length - pow(2, size_), width - pow(2, size_), height - pow(2, size_))

Box = namedtuple('Box', 'size number')

length, width, height = input().split()
length, width, height = int(length), int(width), int(height)

n = int(input())

Boxes = []

for i in range(n):
    size, number = input().split()
    size, number = int(size), int(number)
    Boxes.append(Box(size, number))

Solution(length, width, height)