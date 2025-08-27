def perm(selected: list, remaining: list):
    """
    재귀로 순열을 생성
    Args:
        selected (list[int]): 현재까지 선택된 원소들의 순열
        remaining (list[int]): 아직 선택되지 않은 원소들
    """
    global perm_result

    if not remaining:
        perm_result.append(selected)
        return

    for i in range(len(remaining)):
        pick = remaining[i]
        new_remaining = remaining[:i] + remaining[i+1:]
        perm(selected + [pick], new_remaining)


def get_hit_order():
    """
    선수들의 모든 타순 경우를 반환
    문제에서 1번 선수는 항상 4번타자
      => 8!가지 경우의 수
    """
    global perm_result
    temp = [i for i in range(1, 9)]  # 1부터 8까지 순서를 정하고

    def plus_one_ge_four(x):
        if x >= 4:
            return x + 1
        else:
            return x

    arr = list(map(plus_one_ge_four, temp))   # 1번선수는 4번타자로 넣기 위해 전처리
    perm([], arr)

    for idx in range(len(perm_result)):
        perm_result[idx] = [4] + perm_result[idx]

    return perm_result


def baseball_game(hitting_order, player_performance) -> int:
    """
    타순과, 선수들의 타석 결과가 있을 때 점수를 반환
    Args:
        hitting_order (list[int]): 타순
        player_performance (list[int]): 선수들의 이닝 별 타석 결과
    Returns:
        int: 타순대로 타석에 섰을때 점수 반환
    """
    # 현재 타석에 올라갈 타자 번호 1번 타자 ~ 9번 타자  -> 0~8
    curr_hitter = 0

    out_count = 0
    score = 0
    curr_inning = 1
    end_inning = len(player_performance)

    base_status = 0b000  # 순서대로 3루, 2루, 1루 주자 여부

    while True:

        if curr_inning > end_inning:  # 경기 종료
            return score

        # print(f"[DEBUG] curr_inning: {curr_inning}")
        print(f"[DEBUG] curr_hitter: {curr_hitter}")
        print(f"[DEBUG] hitting_order: {hitting_order}")
        # print(f"[DEBUG] player_performance: {player_performance}")
        # print(f"[DEBUG] player_performance[curr_inning-1]: {player_performance[curr_inning-1]}")

        hitter = hitting_order.index(curr_hitter + 1)  # 타순에서 어느 선수가 칠지 찾기
        hit_result = player_performance[curr_inning - 1][hitter]  # 타석 결과

        if hit_result == 0:  # 아웃이면
            out_count += 1  # 아웃카운트 증가

        else:  # 안타이상을 치면

            # 타자와 주자 진루
            base_status = base_status << hit_result  # 주자 진루
            base_status += 2 ** (hit_result - 1)  # 타자 진루

            # 홈에 들어온 선수가 있는 지 확인
            home_base = base_status >> 3
            score_got = 0

            for _ in range(4):  # 홈런 시 최대 4명
                if home_base & 0b1 == 1:  # 비트 연산으로 한 명씩 체크
                    score_got += 1
                    home_base >>= 1

            score += score_got  # 전체 스코어에 기록

        curr_hitter = (curr_hitter + 1) % 9

        # print(f"[DEBUG]: hit_result: {hit_result}")
        # print(f"[DEBUG]: out_count: {out_count}")

        if out_count == 3:  # 아웃이 3개면
            curr_inning += 1  # 다음 이닝
            out_count = 0  # 아웃카운트 초기화


def open_input_as_stdin():
    import sys
    sys.stdin = open("input_17281.txt")


def main():
    global perm_result
    T = int(input())

    for tc in range(1, T+1):
        perm_result.clear()
        N = int(input())
        given_input = [list(map(int, input().split())) for _ in range(N)]
        hit_order = get_hit_order()

        # print(f"[DEBUG] hit_order: {hit_order}")

        score_case = []
        for n, order in enumerate(hit_order):
            # print(f"[DEBUG] {n}th_game")
            score_case.append(baseball_game(order, given_input))
        # score_case.append(baseball_game([4,1,2,3,5,6,7,8,9], given_input))
        result = max(score_case)

        print(f"#{tc} {result}")


if __name__ == "__main__":
    open_input_as_stdin()
    perm_result = []
    main()
