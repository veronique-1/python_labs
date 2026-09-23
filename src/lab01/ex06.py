n = int(input())

ochny = 0   
zaochny = 0  

for i in range(n):
    line = input().split()
    if_ochny= line[3] == "True"

    if if_ochny:
        ochny += 1
    else:
        zaochny += 1

print(ochny, zaochny)