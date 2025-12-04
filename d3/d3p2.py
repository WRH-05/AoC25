total_sum = 0

with open("d3/d3p1.txt", "r") as file:
    for line in file:
        line = line.strip()
        
        # pot of greed: pick the 12 largest digits in order
        result = []
        remaining = line
        
        for _ in range(12):
            if not remaining:
                break
            best_idx = 0
            for i in range(len(remaining) - (12 - len(result)) + 1):
                if remaining[i] > remaining[best_idx]:
                    best_idx = i
            result.append(remaining[best_idx])
            remaining = remaining[best_idx + 1:]
        
        max_combination = int(''.join(result))
        total_sum += max_combination

print(total_sum)