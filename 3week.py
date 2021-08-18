# 퍼즐 조각 채우기
from collections import deque

# 블럭의 연결상태를 배열로 가져옴
def get_block(board, target):
    n = len(board)
    # board == 가져온 리스트
    # target 빈공간을 찾을지 채워진 공간을 찾을지 선택
    q = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    arr = [[] for _ in range(7)]
    # 각각 구해서 왼쪽위로 땡김 (숫자, 좌표들)
    for i in range(n):
        for j in range(n):
            if board[i][j] == target:
                temp = []
                q.append((i, j))
                board[i][j] = not target
                count = 1
                # 연결된 블럭의 숫자와 좌표를 temp에 저장
                while q:
                    x, y = q.popleft()
                    temp.append((x, y))
                    for direction in range(4):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n and board[nx][ny] == target:
                            q.append((nx, ny))
                            board[nx][ny] = not target
                            count += 1
                # 최소x, y를 각 죄표에서 뺀 값을 저장해 모양을 왼쪽위로 옮김(비교를 쉽게 하기 위함)
                min_x = 51
                min_y = 51
                for x, y in temp:
                    min_x = min(x, min_x)
                    min_y = min(y, min_y)
                arr[count].append(sorted([(temp[index][0] - min_x, temp[index][1] - min_y) for index in range(len(temp))]))
    return arr

# 회전결과 4개를 모두 반환
def rotate_block(block):
    temp_block = [[] for _ in range(4)]
    new_block = []
    offset = 50
    for x, y in block:
        temp_block[0].append((x + offset, y + offset))
    for x, y in block:
        temp_block[1].append((-y + offset, x + offset))
    for x, y in block:
        temp_block[2].append((y + offset, -x + offset))
    for x, y in block:
        temp_block[3].append((-x + offset, -y + offset))

    for i in range(4):
        min_x = 51
        min_y = 51
        for x, y in temp_block[i]:
            min_x = min(x, min_x)
            min_y = min(y, min_y)
        new_block.append(sorted([(block[0] - min_x, block[1] - min_y) for block in temp_block[i]]))

    return new_block

# 구멍에 맞는 블럭인지 확인
def is_fit(hole, block):
    blocks = rotate_block(block)
    for block in blocks:
        if hole == block:
            return True

    return False

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]] # 14
# game_board = [[0,0,0],[1,1,0],[1,1,1]]	
# table = [[1,1,1],[1,0,0],[0,0,0]]
answer = 0

blank = get_block(game_board, 0)
puzzle = get_block(table, 1)

for i in range(1, 7):
    for shape in blank[i]:
        for puz in puzzle[i]:
            if is_fit(shape, puz):
                answer += i
                puzzle[i].remove(puz)
                break

print(answer)