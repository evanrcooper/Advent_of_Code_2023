file = open("input.txt", "r")
lines = file.readlines()
file.close()

def isAdjacent(lines, i, j):
    if i-1 >= 0:
        if j-1 >= 0:
            if lines[i-1][j-1] != '.':
                if not lines[i-1][j-1].isdigit():
                    return True
        if j+1 < len(lines[i-1]):
            if lines[i-1][j+1] != '.':
                if not lines[i-1][j+1].isdigit():
                    return True
        if j < len(lines[i-1]):
            if lines[i-1][j] != '.':
                if not lines[i-1][j].isdigit():
                    return True
            
    if j-1 >= 0:
        if lines[i][j-1] != '.':
            if not lines[i][j-1].isdigit():
                    return True
        
    if j+1 < len(lines[i]):
        if lines[i][j+1] != '.':
            if not lines[i][j+1].isdigit():
                    return True
        
    if i+1 < len(lines):
        if j-1 >= 0:
            if lines[i+1][j-1] != '.':
                if not lines[i+1][j-1].isdigit():
                    return True
        if j+1 < len(lines[i+1]):
            if lines[i+1][j+1] != '.':
                if not lines[i+1][j+1].isdigit():
                    return True
        if j < len(lines[i+1]):
            if lines[i+1][j] != '.':
                if not lines[i+1][j].isdigit():
                    return True
    return False

sum = 0

for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        digits = ""
        if lines[i][j].isdigit():
            if isAdjacent(lines, i, j):
                while j >= 0 and lines[i][j].isdigit():
                    j -= 1
                j += 1
                while j < len(lines[i]) and lines[i][j].isdigit():
                    digits += lines[i][j]
                    j += 1
                # print(digits)
                sum += int(digits)
        j += 1

print(sum)