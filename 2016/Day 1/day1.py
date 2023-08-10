# Link: https://adventofcode.com/2016/day/1
coord = (0,0)
seqString = 'R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1'
seqTest = 'R5, R5, R2'

def getDirection(angle, move):
    if move[0] == 'L':
        return (angle-1) % 4
    elif move[0] == 'R':
        return (angle+1) % 4
    else:
        return angle % 4
    
def getDirectionList(angle, seq):
    dirList = []
    seqList = seq.split(', ')
    for i in seqList:
        angle = getDirection(angle, i)
        dirList.append((i[0], angle))
    return dirList

def getMove(angle, coord, move):
    newAngle = getDirection(angle, move)
    moveDistance = int(move[1:])
    moveMultiplier = [(0,1),(1,0),(0,-1),(-1,0)]
    multiplier = moveMultiplier[newAngle]
    return (coord[0] + multiplier[0]*moveDistance, coord[1] + multiplier[1]*moveDistance), newAngle

def getMoveFull(angle, coord, move):
    moveSteps = []
    newAngle = getDirection(angle, move)
    moveDistance = int(move[1:])
    moveMultiplier = [(0,1),(1,0),(0,-1),(-1,0)]
    multiplier = moveMultiplier[newAngle]
    for i in range(moveDistance):
        coord = (coord[0] + multiplier[0]*1, coord[1] + multiplier[1]*1)
        moveSteps.append(coord)
    return moveSteps, newAngle
    
def getCoord(coord, seq):
    coordList = []
    angle = 0
    moveList = seq.split(', ')
    for move in moveList:
        coord, angle = getMove(angle, coord, move)
        coordList.append(getMove(angle, coord, move)[0])
    return coord, coordList

def getCoordFull(coord, seq):
    coordFullList = []
    angle = 0
    moveList = seq.split(', ')
    for move in moveList:
        fullMoveSteps, angle = getMoveFull(angle, coord, move)
        for i in range(len(fullMoveSteps)):
            coordFullList.append(fullMoveSteps[i])
        coord = fullMoveSteps[-1]
    return coord, coordFullList

def findRevisit(coordList):
    coordSet = set()
    for i in coordList:
        uniqueLen = len(coordSet)
        coordSet.add(i)
        if len(coordSet) == uniqueLen:
            return i
    
moveString = input()

# Part 1
finalCoord, coordList = getCoord(coord, moveString)
print(finalCoord)
print("Part 1:", abs(finalCoord[0])+abs(finalCoord[1]),"\n")

# Part 2
finalFullCoord, coordFullList = getCoordFull(coord, moveString)
firstIntersect = findRevisit(coordFullList)
print(firstIntersect)
print("Part 2:", abs(firstIntersect[0])+abs(firstIntersect[1]))
