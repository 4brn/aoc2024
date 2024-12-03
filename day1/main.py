with open("input.txt", "r") as file:
    data = file.readlines() 
    file.close()

left = []
right = []

for line in data:
    line = line.strip().split()
    if not line:
        continue
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

sum = 0
for lnum, rnum in zip(left, right):
    sum += abs(lnum - rnum)

print(sum)
