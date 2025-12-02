data = []
sum = 0

with open("d2/d2p1.txt", "r") as file:
    for line in file:
        main_parts = line.strip().split(',')
        data.append([part.split('-') for part in main_parts])

for item in data:
    for a, b in item:
        ids = range(int(a), int(b)+1)
        for n in ids:
            if len(str(n)) % 2 != 0:
                continue
            else:
                split_point = int(len(str(n))/2)
                if str(n)[:split_point] == str(n)[split_point:]:
                    sum += n
                else:
                    continue
        
print(sum)