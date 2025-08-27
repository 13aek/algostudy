import sys
from itertools import combinations

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

result = 1e9

for comb in combinations([i for i in range(1,N)], N//2 - 1):
    start_set = set(comb).union(set([0]))
    link_set = set([i for i in range(N)]) - start_set
    start = list(start_set)
    link = list(link_set)
    start_power, link_power = 0, 0 
    for i, r in zip(start,link):
        for j, c in zip(list(start_set - set([i])), list(link_set - set([r]))):
            start_power += matrix[i][j] 
            link_power += matrix[r][c] 
    if start_power == link_power: 
        result = 0
        break
    result = min(result, abs(start_power - link_power))

print(f'{result}')