# Test the dial logic with a simple example
def count_passes_through_zero(start_pos, movement, direction):
    """Count how many times we pass through or land on 0"""
    count = 0
    current = start_pos
    
    if direction == "L":
        for i in range(movement):
            current = (current - 1) % 100
            if current == 0:
                count += 1
                if i < 10 or movement - i <= 3:  # Print first 10 and last 3
                    print(f"  Step {i+1}/{movement}: Hit 0")
    else:  # "R"
        for i in range(movement):
            current = (current + 1) % 100
            if current == 0:
                count += 1
                if i < 10 or movement - i <= 3:
                    print(f"  Step {i+1}/{movement}: Hit 0")
    
    return count, current

# Test case 1: Move right 120 from position 80
count, end = count_passes_through_zero(80, 120, "R")
print(f"R120 from 80: passes through 0 {count} times, ends at {end}")

# Test case 2: Move left 60 from position 50
count, end = count_passes_through_zero(50, 60, "L")
print(f"L60 from 50: passes through 0 {count} times, ends at {end}")

# Test case 3: Move right 50 from position 50  
count, end = count_passes_through_zero(50, 50, "R")
print(f"R50 from 50: passes through 0 {count} times, ends at {end}")

# Test case 4: Move right 100 from position 0
count, end = count_passes_through_zero(0, 100, "R")
print(f"R100 from 0: passes through 0 {count} times, ends at {end}")

# Test case 5: Move left 100 from position 0
count, end = count_passes_through_zero(0, 100, "L")
print(f"L100 from 0: passes through 0 {count} times, ends at {end}")

# Now test the formula
print("\nTesting formula:")
for start, movement, direction in [(80, 120, "R"), (50, 60, "L"), (50, 50, "R"), (0, 100, "R"), (0, 100, "L"), (0, 1, "L"), (0, 1, "R"), (0, 50, "L"), (0, 50, "R")]:
    if direction == "L":
        formula_count = movement // 100
        if movement % 100 > start:
            formula_count += 1
        end_pos = (start - movement) % 100
    else:
        formula_count = movement // 100
        if start + (movement % 100) >= 100:
            formula_count += 1
        end_pos = (start + movement) % 100
    
    actual_count, actual_end = count_passes_through_zero(start, movement, direction)
    match = "✓" if formula_count == actual_count else "✗"
    print(f"{match} {direction}{movement} from {start}: formula={formula_count}, actual={actual_count}, end={end_pos}")
