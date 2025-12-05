id_ranges = []
available_ids = []
fresh_id_ranges = []
s = []
fresh_id_range_len = 0
fresh_ids = 0
rotten_ids = 0

with open("d5/d5p1.txt", "r") as file:
    lines = file.readlines() 

for line in lines:
    line = line.strip()
    if line == "": 
        break
    if "-" in line:
        id_ranges.append(list(line.split("-")))

start_index = len(id_ranges) + 1  
for i in range(start_index, len(lines)):
    line = lines[i].strip()
    if line == "":
        continue
    if "-" not in line: 
        available_ids.append(line)

for i in available_ids:
    is_fresh = False
    for j in id_ranges:
        if int(j[0]) < int(i) < int(j[1]):
            is_fresh = True
            fresh_ids += 1
            fresh_id_ranges.append(range(int(j[0]), int(j[1])))
            fresh_id_range_len += len(fresh_id_ranges)
            fresh_id_ranges.clear
            break
        
    if not is_fresh:
            rotten_ids +=1



print(f"fresh ids:{fresh_ids}")
print(f"rotten ids:{rotten_ids}")
print(f"fresh id length:{fresh_id_range_len}")