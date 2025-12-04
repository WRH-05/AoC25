total_sum = 0

with open("d3/d3p1.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        max_combination = 0
        
        # Try every pair of positions (i, j) where i comes before j
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Combine the digits at position i and j
                two_digit = int(line[i] + line[j])
                if two_digit > max_combination:
                    max_combination = two_digit
        
        total_sum += max_combination
            
print(total_sum)

print(len(line))
