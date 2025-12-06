import time

start_time = time.time()

id_ranges = []
available_ids = []
fresh_count = 0

with open("d5/d5p1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if line == "":
        break
    if "-" in line:
        parts = line.split("-")
        id_ranges.append((int(parts[0]), int(parts[1])))

start_index = len(id_ranges) + 1
for i in range(start_index, len(lines)):
    line = lines[i].strip()
    if line:
        available_ids.append(int(line))

for available_id in available_ids:
    is_fresh = False
    for start, end in id_ranges:
        if start <= available_id <= end:
            is_fresh = True
            break
    if is_fresh:
        fresh_count += 1

print(f"Fresh ingredient IDs: {fresh_count}")

end_time = time.time()
elapsed_time = (end_time - start_time) * 1000
print(f"Execution time: {elapsed_time:.2f} ms")