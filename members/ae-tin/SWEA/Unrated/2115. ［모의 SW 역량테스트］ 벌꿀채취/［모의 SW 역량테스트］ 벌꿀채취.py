def DFS(arr, used, depth, s):
    global max_v

    if s > C: return
    elif depth == M:
        # if s > C: return
        # else:
        profit = sum([ v*v if tf else 0 for v, tf in zip(arr, used)])
        max_v = max([max_v, profit])
        return
        
    # elif s > C: return
    
    used[depth] = False
    DFS(arr, used, depth + 1, s) # 안쓰니까 더해주면 안됨
    
    used[depth] = True
    DFS(arr, used, depth + 1, s + arr[depth]) # 쓰는거 더해주고

    
    
   
    
T = int(input())

for test_case in range(1,T+1):
    

    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    possibility_same_row = N-M >= M

    result = 0
    # 4중 for문으로 두 양봉자 선택
    for i in range(N): # 행은 모두 가능
        for j in range(N-M+1): # 열은 N-M 인덱스까지 선택가능
            for r in range(i, N):
                for c in range(N-M+1):
                    if i == r:
                        if not possibility_same_row: continue
                        else: 
                            # 이때만 가능
                            if j+M <= c:
                                first = matrix[i][j:j+M] 
                                second = matrix[r][c:c+M]
                            else: continue
                    else:
                        first = matrix[i][j:j+M] 
                        second = matrix[r][c:c+M]

                    if sum(first) <= C: 
                        profit1 = sum([i*i for i in first])
                    else: # 부분집합
                        max_v = 0
                        used = [False] * M
                        DFS(first, used, 0, 0) # 배열, depth, sum
                        profit1 = max_v

                    if sum(second) <= C: 
                        profit2 = sum([i*i for i in second])
                    else: # 부분집합
                        max_v = 0
                        used = [False] * M
                        DFS(second, used, 0, 0)
                        profit2 = max_v
                    result = max([result, profit1 + profit2])


    print(f'#{test_case} {result}')