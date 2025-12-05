import time

start_time = time.time()

id_ranges = []

with open("d5/d5p1.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            break
        if "-" in line:
            parts = line.split("-")
            id_ranges.append((int(parts[0]), int(parts[1])))

print(f"Fresh ingredient ID ranges:")
for r in id_ranges:
    print(f"  {r[0]}-{r[1]}")

# Sort ranges by start value
id_ranges.sort()

# Merge overlapping ranges
merged = [id_ranges[0]]

for current_start, current_end in id_ranges[1:]:
    last_start, last_end = merged[-1]
    
    # If ranges overlap or are adjacent, merge them
    if current_start <= last_end + 1:
        merged[-1] = (last_start, max(last_end, current_end))
    else:
        merged.append((current_start, current_end))

# Calculate total unique IDs
total_fresh = 0
for start, end in merged:
    # Count IDs from start to end (inclusive)
    count = end - start + 1
    total_fresh += count
    print(f"Range ({start}-{end}): {count} IDs")

print(f"\nTotal fresh ingredient IDs: {total_fresh}")

end_time = time.time()
elapsed_time = (end_time - start_time) * 1000
print(f"Execution time: {elapsed_time:.2f} ms")