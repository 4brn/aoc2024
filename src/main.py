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

similarity = {}
for num in right:
    if num in similarity.keys():
        similarity[num] += 1
    else:
        similarity[num] = 1

sum = 0
for num in left:
    if num in similarity.keys():
        sum += num * similarity[num]

print(sum)

