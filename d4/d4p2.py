with open("d4/d4p1.txt", "r") as file:
    data_listed = [list(line.strip()) for line in file]

# Store all marked points across all iterations
all_marked_points = []

# Get dimensions
rows = len(data_listed)
cols = len(data_listed[0]) if rows > 0 else 0

# Keep running until no more @ symbols with < 4 adjacent @ are found
while True:
    marked_points = []
    
    # Check each position
    for i in range(rows):
        for j in range(cols):
            # Only check if current position is @
            if data_listed[i][j] == '@':
                adjacent_count = 0
                
                # Check all 8 surrounding positions
                directions = [
                    (-1, -1), (-1, 0), (-1, 1),  # Top row
                    (0, -1),           (0, 1),    # Left and right
                    (1, -1),  (1, 0),  (1, 1)     # Bottom row
                ]
                
                for dx, dy in directions:
                    new_i = i + dx
                    new_j = j + dy
                    
                    # Check if the position is within bounds
                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        # Check if it's an @
                        if data_listed[new_i][new_j] == '@':
                            adjacent_count += 1
                
                # Mark if less than 4 adjacent @s
                if adjacent_count < 4:
                    marked_points.append((i, j))
    
    # If no more @ symbols with < 4 adjacent @ were found, stop
    if len(marked_points) == 0:
        break
    
    # Convert the marked @ symbols to .
    for i, j in marked_points:
        data_listed[i][j] = '.'
        all_marked_points.append((i, j))

print(f"Total marked points: {len(all_marked_points)}")
print(f"First 10 marked points: {all_marked_points[:10]}")