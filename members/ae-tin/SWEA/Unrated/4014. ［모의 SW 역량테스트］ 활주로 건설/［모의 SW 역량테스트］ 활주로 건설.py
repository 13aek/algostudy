def test(lst, X):

    prev = lst[0]
    cnt = 0 # 숫자가 바뀌면 계속 초기화
    road_state = 0 #층이 낮아졌을 때 활주로 건설 상태 표시
    road_comp = 0 #공사 끝낸 시점 확인
    # 층이 높아질 땐 그제서야 돌아온길에 활주로 건설 확인
    for i in lst:
        diff = i - prev
        #활주로 건설 안됨
        if abs(diff) > 1 : return False
        #활주로 건설 가능
        else:
            #차이가 없을땐 갯수 세기
            if diff == 0 :
                cnt += 1
                prev = i
                #공사중이라면
                if road_state != 0:
                    road_state += 1
                    if road_state == X:
                        road_state = 0
                        road_comp = 1
                #공사중 아니라면
                else:
                    # 공사를 끝낸 상태
                    if road_comp == 1:
                        if cnt >= 2*X: road_comp = 0

            #낮아지면 경사로 설치 준비
            elif diff == -1 :
                cnt = 1
                prev = i
                # 설치중이 아님
                if road_state == 0:
                    # 설치중으로 표시
                    road_state = 1

                # 설치 중이었다면
                else: return False
                
            #높아지면 이전에 경사로 설치할 수 있나 확인
            elif diff == 1:
                #경사로 길이(X)보다 작으면 안됨, 공사중이었으면 안됨
                if cnt < X or road_state != 0 or road_comp == 1: return False
                else:
                    cnt = 1
                    prev = i
                    road_comp = 0
    else:
        if road_state != 0: return False
        if diff == 1: False
    return True
            
T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        if test(matrix[i], X): result += 1
        rev = [lst[i] for lst in matrix]
        if test(rev, X): result += 1


    print(f'#{tc} {result}')