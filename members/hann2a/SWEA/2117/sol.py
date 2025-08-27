import sys

sys.stdin = open('input.txt', 'r')

cost = [(k*k + (k-1)*(k-1)) for k in range(40)]
 
def solve1():
    ans = 0
    # [1] home 배열 생성
    home=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))
 
    # [2] 모든좌표 순회하면서, dist배열만들고, cnt
    for si in range(N):
        for sj in range(N):
            dist = [0]*40
            for hi,hj in home:
                t = abs(si-hi)+abs(sj-hj)+1
                dist[t] += 1
 
            cnt = 0
            for k in range(1, 40):
                cnt += dist[k]
                if cost[k] <= cnt * K and ans < cnt:
                    ans = cnt
    return ans
 
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve1()
 
    print(f'#{test_case} {ans}')