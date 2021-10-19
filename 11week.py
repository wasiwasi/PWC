# 아이템 줍기
rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
# [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
# [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]	9	7	6	1	11
# [[1,1,5,7]]	1	1	4	7	9
# [[2,1,7,5],[6,4,10,10]]	3	1	7	10	15
# [[2,2,5,5],[1,3,6,4],[3,1,4,6]]	1	4	6	3	10
# nx, ny 탐색시 겹치는 노드가 생겨 도형의 크기를 두배로 늘림
MAX_WORLD = 102
start_x = characterY * 2
start_y = characterX * 2
end_x = itemY * 2
end_y = itemX * 2
world = [[False] * MAX_WORLD for _ in range(MAX_WORLD)]
# 테두리를 포함해 True로 채움
for x1, y1, x2, y2 in rectangle:
    for i in range(y1 * 2, y2 * 2 + 1):
        for j in range(x1 * 2, x2 * 2 + 1):
            world[i][j] = True
# 테두리만 남기고 내용을 False로 초기화
for x1, y1, x2, y2 in rectangle:
    for i in range(y1 * 2 + 1, y2 * 2):
        for j in range(x1 * 2 + 1, x2 * 2):
            world[i][j] = False

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

count = 0
stack = [(start_x, start_y)]
# 스택에 시작점을 넣어 아이템이 나올때 까지 탐색
while(stack):
    x, y = stack.pop()
    world[x][y] = False
    count += 1
    if (x, y) == (end_x, end_y):
        min_value = count
        count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if world[nx][ny] == True:
            stack.append((nx, ny))
            # break가 없으면 꼭짓점에서 두개씩 들어감
            break

# count는 아이템에서 시작점으로 돌아왔을 때의 코스트
min_value = min(min_value, count)

print(min_value // 2)