import sys
import itertools

# sys.stdin = open('input.txt')

def calculate_ability(member, ability):

    ability_sum = 0

    for i in member:
        for j in member:
            ability_sum += ability[i][j]
    
    return ability_sum


N = int(input())

people = [] 

for i in range(N):
    people.append(i)

ability = [list(map(int, input().split())) for _ in range(N)]

difference = []

teams = itertools.combinations(people, N // 2)

for team_start in teams:
    team_link = list(set(people) - set(team_start))

    start_ability = calculate_ability(team_start, ability)
    link_ability = calculate_ability(team_link, ability)

    difference.append(abs(start_ability - link_ability))

print(min(difference))