import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

second_supervisor = [max(math.ceil((student-B)/C),0) for student in A]
result = N + sum(second_supervisor)

print(result)
