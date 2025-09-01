T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def DFS(node, direc, each_len, path):
    global max_v
    i, j = node

    # 종료 조건
    if node == start_point and len(path) != 1:
        max_v = max([max_v, len(path)-1]) # 맨처음거 빼줌
        
        return

    
    # 직진할 때는 맨처음 한 변이랑 마지막 방향일 때
    if direc == 3 or (direc == 0 and len(path) == 1):
        # print('...')
        r, c = i + dr[direc], j + dc[direc]
        if 0 <= r < N and 0 <= c < N:
            if matrix[r][c] not in path or (r,c) == start_point:  
                each_len[direc] += 1
                path.append(matrix[r][c])
                # print('직전',(r,c), path)
                DFS((r,c), direc, each_len, path)

                path.pop()
                each_len[direc] -= 1
    # 나머지는 분기가 있음
    elif direc in [0, 1, 2]:
        # print('....')
        for k in range(2):
            direc += k
            r, c = i + dr[direc], j + dc[direc]
            # print(r,c, direc, matrix[r][c])
            if 0 <= r < N and 0 <= c < N:
                if matrix[r][c] not in path or (r,c) == start_point:    
                    each_len[direc] += 1
                    path.append(matrix[r][c])
                    # print(f'분기{k}',(r,c), path, direc)
                    DFS((r,c), direc, each_len, path)
                    path.pop()
                    each_len[direc] -= 1
    # return

'''
젤 윗 꼭지점에서만 시작해서 델타로 BFS 탐색.
마지막에 처음 좌표 오면 종료.
델타는 좌하 -> 우하 -> 우상 -> 좌상 순으로 진행.
방향 변수를 줘서 방향 조절.
변마다 [1변, 2변, 3변, 4변] 으로 변 길이 기록. 방향 변수 변할 때마다 인덱스 변화
'''                

for testcase in range(1,T+1):
    N  = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 무조건 윗 꼭짓점에서 시작한다고 하면 스타트점은 [1,N-2] 열인덱스, [0,N-3] 행인덱스만 돌아야함
    # (x, y, 방향, cnt)
    start_points = [ (i, j, 0, [0]*4, [matrix[i][j]]) for i in range(0, N-2) for j in range(1, N-1)]

    dr = [1, 1, -1, -1] # 좌하, 우하, 우상, 좌상 순 
    dc = [-1, 1, 1, -1]
    d = 0 # 0 1 2 3 차례대로 방향
    d_length = [0]*4

    max_v = -1

    for i, j, direc, each_len, path in start_points:
        start_point = (i, j)
        DFS((i, j), direc, each_len, path)
            
    print(f'#{testcase} {max_v}')