file = open('input.txt', 'r')

lines = file.readlines()

def extractDigits(line):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(int(c))
        else:
            match c:
                case 'z': # zero
                    if (len(line) >= 4+i):
                        if line[i:i+4] == "zero":
                            digits.append(0)
                case 'o': # one
                    if (len(line) >= 3+i):
                        if line[i:i+3] == "one":
                            digits.append(1)
                case 't': #two, three
                    if (len(line) >= 5+i):
                        if line[i:i+5] == "three":
                            digits.append(3)
                    if (len(line) >= 3+i):
                        if line[i:i+3] == "two":
                            digits.append(2)
                case 'f': # four, five
                    if (len(line) >= 4+i):
                        if line[i:i+4] == "four":
                            digits.append(4)
                        elif line[i:i+4] == "five":
                            digits.append(5)
                case 's': # six, seven
                    if (len(line) >= 5+i):
                        if line[i:i+5] == "seven":
                            digits.append(7)
                    if (len(line) >= 3+i):
                        if line[i:i+3] == "six":
                            digits.append(6)
                case 'e': # eight
                    if (len(line) >= 5+i):
                        if line[i:i+5] == "eight":
                            digits.append(8)
                case 'n': # nine
                    if (len(line) >= 4+i):
                        if line[i:i+4] == "nine":
                            digits.append(9)
    return digits


sum = 0

for line in lines:
    digits = extractDigits(line)
    # print(digits, end=' ')
    add = int(digits[0])*10
    add += digits[-1]
    # print(add)
    sum += add

print(sum)