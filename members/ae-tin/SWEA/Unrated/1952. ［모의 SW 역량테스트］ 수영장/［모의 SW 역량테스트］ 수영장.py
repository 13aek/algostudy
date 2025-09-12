def recur(month,total_cost):
    global min_answer
    if month >11:
        # todo : 최소값 갱신
        min_answer = min(min_answer, total_cost)
        return
    
    # 1일권 모두
    recur(month + 1, total_cost + (plans[month]* fees[0]))
    # 1달권으로 모두
    recur(month + 1, total_cost + (fees[1]))
    # 3달권으로 모두
    recur(month + 3, total_cost + (fees[2]))
    # 1년권으로 모두
    recur(month + 12, total_cost + (fees[3]))

T = int(input())

for test_case in range(1,T+1):
    fees = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    min_answer = 1e9 # 정답이 항상 보장되는경우
    #min_answer = 10000*N # 나올 수 없다면 최대 값으로
    recur(0,0)

    print(f'#{test_case} {min_answer}')