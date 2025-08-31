import copy

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def test(matrix):
    test_pass = 0
    for i in range(W): #층 검사
        for j in range(D): # 연속 검사
            if j == 0 : 
                prev = matrix[j][i] 
                cnt = 1
            else:
                if matrix[j][i] == prev:
                    cnt += 1
                elif matrix[j][i] != prev:
                    cnt = 1
                    prev = matrix[j][i]

                if cnt == K : 
                    test_pass += 1
                    break
        if test_pass != i+1 :
            return False
    else: return True

def DFS(matrix,depth,p_type,cnt):
    global min_v        

    if depth == D:
        if test(matrix): 
            # if cnt == 3:
            
            if cnt < min_v : 
                min_v = cnt
                # for l in range(D):
                #     print(matrix[l])
                # print(cnt)
            return cnt
        else:
            return False
    
    
    # 아무것도 안하기
    matrix[depth] = matrix_origin[depth]
    TF = DFS(matrix,depth+1,False,cnt)
 #   if TF: return TF

    # A로 바꾸기
    cnt +=1
    matrix[depth] = As
    TF =DFS(matrix,depth+1,'A',cnt)
 #   if TF: return TF

    # B로 바꾸기
    matrix[depth] = Bs
    TF = DFS(matrix,depth+1,'B',cnt)
 #   if TF: return TF
        
    
                

for testcase in range(1,T+1):
    D, W, K  = map(int,input().split())
    matrix_origin = [list(map(int,input().split())) for _ in range(D)] 
    matrix_rep = copy.deepcopy(matrix_origin) 
    As, Bs = [0]*W, [1]*W # 약품처리 조합은 A발랐을 때, B발랐을 때, 안발랐을 때 3가지 경우 고려
    # for l in range(D):
    #     print(matrix_origin[l])
    # print('***')
    cnt = 0
    min_v = 1e9
    # DFS 돌면서 검사. 
    if test(matrix_origin): 
        print(f'#{testcase} {cnt}')
    else:
        result = DFS(matrix_rep,0,False,cnt)
            
        print(f'#{testcase} {min_v}')