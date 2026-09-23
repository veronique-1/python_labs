n = int(input(f'in_1: '))

ochny = 0   
zaochny = 0  

for i in range(n):
    line = input(f'in_{i+2}: ').split()
    if_ochny= line[3] == "True"

    if if_ochny:
        ochny += 1
    else:
        zaochny += 1

print(ochny, zaochny)