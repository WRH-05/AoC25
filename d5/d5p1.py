

with open("d5/d5p1.txt", "r") as file:
    for line in file:
        id_ranges = list(line.strip().split("-"))
        print(id_ranges)
        if id_ranges == []:
            break
        
