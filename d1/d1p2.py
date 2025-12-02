current_dial = 50
combs = []
hits = 0

with open("d1/d1p2.txt", "r") as file:
    for line in file:
        combs.append(line.strip())
 
for comb in combs:
    if comb[0] == "L":
        movement = int(comb[1:])
        hits += movement // 100
        if current_dial > 0 and movement % 100 > current_dial:
            hits += 1
        current_dial = (current_dial - movement) % 100
    else:
        movement = int(comb[1:])
        hits += movement // 100
        if current_dial + (movement % 100) >= 100:
            hits += 1
        current_dial = (current_dial + movement) % 100

print(hits)