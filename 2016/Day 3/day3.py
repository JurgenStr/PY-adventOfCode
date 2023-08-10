# Link: https://adventofcode.com/2016/day/3
import os

def triangleCheck(sizeGrid):
    triangleCount = 0
    for i in sizeGrid:
        elements = i.split()
        numbers = [int(j) for j in elements]
        if max(numbers) < sum(numbers)-max(numbers):
            triangleCount += 1
    return triangleCount


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'triangleList.txt')) as f:
    sizeGrid = f.read()
print(sizeGrid)
sizeGrid = sizeGrid.split('\n')
print(triangleCheck(sizeGrid))