def squared_sum(numbers: list):
    result = [number ** 2 for number in numbers]
    return sum(result)


def dfs(cr, cc, selected, honey_amounts, first=True):
    global ans

    # 종료 조건 - 조기종료

    # 방문행동
    picked_honey = arr[cr][cc: cc + M]
    curr_honey = 0

    if sum(picked_honey) <= C:
        curr_honey = squared_sum(picked_honey)
        honey_amounts += curr_honey

    # 합이 C를 초과하면 부분집합 생성 후 최대를 선택
    else:
        for i in range(1 << M):
            result = []
            for j in range(M):
                if i & (1 << j):
                    result.append(picked_honey[j])

                    if sum(result) <= C:
                        curr_honey = max(curr_honey, squared_sum(result))

        # 최대값을 찾은 후 누적
        honey_amounts += curr_honey

    # 종료 조건 - 정답 처리
    if first is False:
        ans = max(ans, honey_amounts)

        # 재귀 호출
    if first:  # 첫 번째 일꾼
        for idx in range(M):
            selected[cr][cc + idx] = True

        for nr in range(cr, N):
            for nc in range(N - M + 1):

                # 미 방문 지역만 갈 예정
                if selected[nr][nc] is False:
                    dfs(nr, nc, selected, honey_amounts, first=False)


T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    selected = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N - M + 1):
            dfs(row, col, selected, 0, first=True)

    print(f"#{tc} {ans}")
