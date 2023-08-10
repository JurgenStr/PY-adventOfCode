# Link: https://adventofcode.com/2016/day/3
import os
from itertools import islice

def triangleCheck(sizeGrid):
    triangleCount = 0
    for i in sizeGrid:
        elements = i.split()
        numbers = [int(j) for j in elements]
        if max(numbers) < sum(numbers)-max(numbers):
            triangleCount += 1
    return triangleCount
    
def triangleCheckPartTwo(sizeGrid):
    triangleCount = 0
    for i in range(3, len(sizeGrid)+1, 3):
        transposeQueue = []
        for j in sizeGrid[i-3:i]:
            elements = j.split()
            transposeQueue.append(int(element) for element in elements)
        transposeQueue = list(zip(*transposeQueue))
        for j in transposeQueue:
            if max(j) < sum(j)-max(j):
                triangleCount += 1
    return triangleCount
        
# Part 1
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'triangleList.txt')) as f:
    sizeGrid = f.read()
sizeGrid = sizeGrid.split('\n')
print("Part 1: ", triangleCheck(sizeGrid))

# Part 2
# Quiz demands vertical check, we try to do 3x3 at a time instead
print("Part 2: ", triangleCheckPartTwo(sizeGrid))