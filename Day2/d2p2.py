file = open('input.txt', 'r')
lines = file.readlines()
file.close()

totalPower = 0

for line in lines:
    maxR = 0
    maxG = 0
    maxB = 0
    if line[-1] == '\n':
        line = line[:-1].split(":")[1]
    else:
        line = line.split(":")[1]
    line = line.split(";")
    for round in line:
        round = round.split(",")
        for pick in round:
            print(pick)
            pick = pick.split(" ")[1:]
            match pick[1][0]:
                case 'r':
                    maxR = max(maxR, int(pick[0]))
                case 'g':
                    maxG = max(maxG, int(pick[0]))
                case 'b':
                    maxB = max(maxB, int(pick[0]))
    totalPower += maxR*maxG*maxB

print(totalPower)