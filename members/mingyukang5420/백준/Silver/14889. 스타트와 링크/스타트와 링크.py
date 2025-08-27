def compare_synergies(arr: list) -> int:
    """
    배열에서 시너지를 계산해 차이가 최소일때 그 값을 반환

    Args:
        arr (list[int]): 시너지 정보
    """
    # 전체 인원수
    n = len(arr)
    
    # 팀 짜기
    team_cases = combinations(range(1, n+1), n//2)
    
    # 시너지 차이의 최소값을 기록
    min_diff = 200

    for case in team_cases:  # 왼쪽팀 오른쪽팀 나누기
        left_team = case
        right_team = tuple(element for element in range(1, n+1) if element not in case)
        
        # print(f"[DEBUG] left_team: {left_team}")
        # print(f"[DEBUG] right_team: {right_team}")

        left_synergy = 0
        for left1 in range(n//2):
            for left2 in range(left1, n//2):
                left_synergy += arr[left_team[left1] - 1][left_team[left2] - 1]
                left_synergy += arr[left_team[left2] - 1][left_team[left1] - 1]

        right_synergy = 0
        for right1 in range(n//2):
            for right2 in range(right1, n//2):
                right_synergy += arr[right_team[right1] - 1][right_team[right2] - 1]
                right_synergy += arr[right_team[right2] - 1][right_team[right1] - 1]

        diff = abs(left_synergy - right_synergy)
        if diff < min_diff:
            min_diff = diff 

        # print(f"[DEBUG] diff: {diff}")
        # print(f"[DEBUG] min_diff: {min_diff}")

    return min_diff


# def open_input_as_stdin():
    # import sys
    # sys.stdin = open("input_14889.txt")


def main():
    
    # T = int(input())
    T = 1

    for tc in range(1, T+1):
        
        N = int(input())
        given_input = [list(map(int, input().split())) for _ in range(N)]
        result = compare_synergies(given_input)
       
        # print(f"#{tc} {result}")
        print(result)


if __name__ == "__main__":
    from itertools import combinations
    # open_input_as_stdin()
    main()