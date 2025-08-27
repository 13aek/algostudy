import sys

sys.stdin = open('input.txt', 'r')

# 우하 좌하 좌상 우상 우하(혹시 모르니까)
di=[1, 1, -1, -1, 1]
dj=[1,-1,-1, 1, 1]


# n은 꺾은 횟수 

def dfs(n, ci, cj, v):
    global ans, si, sj

    if n==2 and ans>=len(v)*2:
        return
 
    if n>3:
        return
    
    # 시작 방향은 0(직진)
    # 거기부터 세 번 꺾으면 더 꺾을 수 없음 
    # 따라서 조건 n=3이고, 현재 지점이 시작 지점이며 현재 답보다 방문한 지점이 많을 때
    # ans를 업데이트 
    if n==3 and (ci,cj)==(si,sj) and ans<len(v):
        ans = len(v)
    
    # dr은 direction 
    # n부터 n+1까지 범위 (지금 지점과 다음 지점)
    # 다음 지점은 지금 지점에서 어딘가로 꺾기 
    for dr in range(n, n+2):
        ni,nj = ci+di[dr], cj+dj[dr]
        # 새로운 지점이 배열을 안 넘어가고 아직 방문하지 않았으면 
        # v에 추가 
        # 그리고 방향을 dr, 현재 지점을 ni, nj, 그리고 업데이트된 v를 넣어서 다시 
        # 다녀오면 v를 pop해서 v 초기화 
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(dr, ni, nj, v)
            v.pop()
 
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 업데이트 되지 않으면 -1로 출력되어야 하므로 기본 값 -1 
    ans = -1
    # 배열을 순회하는 시작 지점 
    for si in range(N):
        for sj in range(N):
            v = []
            dfs(0, si, sj, v)
 
    print(f'#{t} {ans}')