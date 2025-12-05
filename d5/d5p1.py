id_ranges = []
available_ids = []
fresh_ranges = set()  # Store range indices that have fresh IDs
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

# Track which range indices have fresh IDs
for i in available_ids:
    is_fresh = False
    for idx, j in enumerate(id_ranges):
        if int(j[0]) < int(i) < int(j[1]):
            is_fresh = True
            fresh_ids += 1
            fresh_ranges.add(idx)  # Mark this range as having fresh IDs
            break
    
    if not is_fresh:
        rotten_ids += 1

# Now calculate the union of all ranges with fresh IDs
all_ids_in_ranges = set()

print(f"fresh ids: {fresh_ids}")
print(f"rotten ids: {rotten_ids}")
print(f"\nRanges with fresh IDs:")

for range_idx in sorted(fresh_ranges):
    j = id_ranges[range_idx]
    range_start = int(j[0])
    range_end = int(j[1])
    range_length = range_end - range_start - 1
    
    # Add all IDs in this range to the union set
    for num in range(range_start + 1, range_end):
        all_ids_in_ranges.add(num)
    
    print(f"Range {range_idx} ({range_start}-{range_end}): length = {range_length}")

print(f"\nTotal unique IDs across all ranges (no overlaps counted twice): {len(all_ids_in_ranges)}")