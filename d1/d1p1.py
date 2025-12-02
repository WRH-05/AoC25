
current_dial = 50
combs = []
hits = 0

with open("d1/d1p1.txt", "r") as file:

    for line in file:
        combs.append(line.strip())
    
for comb in combs:
    if comb[0]=="L":
        int_comb_L = int(comb[1:])
        current_dial = (current_dial - int_comb_L) % 100
    else:
        int_comb_R = int(comb[1:])
        current_dial = (current_dial + int_comb_R) % 100
    
    if current_dial == 0:
        hits += 1

print(hits)