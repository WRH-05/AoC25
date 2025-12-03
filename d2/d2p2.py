data = []
sum = 0

with open("d2/d2p1.txt", "r") as file:
    for line in file:
        main_parts = line.strip().split(',')
        data.append([part.split('-') for part in main_parts])

for item in data:
    for a, b in item:
        ids = range(int(a), int(b)+1)
        for n in ids:
            num_str = str(n)
            length = len(num_str)
            for divisor in range(2, length + 1):
                if length % divisor == 0:
                    chunk_size = length // divisor
                    chunks = [num_str[i:i+chunk_size] for i in range(0, length, chunk_size)]
                    if all(chunk == chunks[0] for chunk in chunks):
                        sum += n
                        break  

print(sum)