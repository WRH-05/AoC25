results = []

with open("d6/d6.txt", "r") as file:
    lines = [line.strip().split() for line in file]

first_op = lines[0] if len(lines) > 0 else []
second_op = lines[1] if len(lines) > 1 else []
third_op = lines[2] if len(lines) > 2 else []
forth_op = lines[3] if len(lines) > 3 else []
ops = lines[4] if len(lines) > 4 else []

def mul(nums):
    product = 1
    for num in nums:
        product *= num
    return product

# Apply operations
for i in range(len(ops)):
    numbers = [int(first_op[i]), int(second_op[i]), int(third_op[i]), int(forth_op[i])]
    
    if ops[i] == "+":
        result = sum(numbers)
    elif ops[i] == "*":
        result = mul(numbers)
    
    results.append(result)

print(results)

final_result = sum(results)
print(final_result)