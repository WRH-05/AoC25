def best_voltage(bank, nums):

    best_voltage = []
    
    while len(best_voltage) < nums:
        remaining = nums - len(best_voltage) - 1
        
        if remaining > 0:
            bank_leaving_enough_digits = bank[:len(bank) - remaining]
        else:
            bank_leaving_enough_digits = bank
        
        largest = max(bank_leaving_enough_digits)
        first_index = bank_leaving_enough_digits.index(largest)
        
        best_voltage.append(largest)
        bank = bank[first_index + 1:]
    
    return int(''.join(best_voltage))

total_sum = 0

with open("d3/d3p1.txt", "r") as file:
    for line in file:
        line = line.strip()
        max_combination = best_voltage(line, 12)
        total_sum += max_combination

print(total_sum)