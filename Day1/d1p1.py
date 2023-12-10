file = open('input.txt', 'r')
sum = 0
while True:
    digits = [0, 0]
    line = file.readline()
    if not line:
        break
    for c in line:
        if c.isdigit():
            digits[0] = ord(c)-ord('0')
            break
    for c in reversed(line):
        if c.isdigit():
            digits[1] = ord(c)-ord('0')
            break
    sum += 10*digits[0]
    sum += digits[1]
print(sum)