import sys
sys.stdin = open('input.txt', 'r')

# 대각선 4방향
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    best = [-1]          # 리스트로 감싸서 참조 공유
    used = [False] * 101

    def dfs(r, c, direction, start_r, start_c, count):
        # 같은 방향 또는 다음 방향만 허용
        for now_d in (direction, direction + 1):
            if now_d >= 4:
                continue

            nr = r + dr[now_d]
            nc = c + dc[now_d]

            # 보드 밖
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 시작점으로 귀환 체크
            if nr == start_r and nc == start_c:
                if now_d == 3 and count >= 4:
                    if count > best[0]:
                        best[0] = count
                continue

            dval = board[nr][nc]
            if used[dval]:
                continue

            used[dval] = True
            dfs(nr, nc, now_d, start_r, start_c, count + 1)
            used[dval] = False

    # 모든 시작점에서 시도
    for start_r in range(N):
        for start_c in range(N):
            used[board[start_r][start_c]] = True
            dfs(start_r, start_c, 0, start_r, start_c, 1)
            used[board[start_r][start_c]] = False

    print(f"#{t} {best[0]}")

