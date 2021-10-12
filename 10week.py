# 교점에 별 만들기
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
# [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# [[0, 1, -1], [1, 0, -1], [1, 0, 1]] ["*.*"]
# [[1, -1, 0], [2, -1, 0]] ["*"]
# [[1, -1, 0], [2, -1, 0], [4, -1, 0]] ["*"]
INF = int(1e9)
point = set()
for i, now in enumerate(line):
    a, b, e = now
    for less in line[i + 1:]:
        # 교점확인
        c, d, f = less
        # 평행 또는 일치
        if a * d - b * c == 0:
            continue
        cx = (b * f - e * d) / (a * d - b * c)
        cy = (e * c - a * f) / (a * d - b * c)
        if int(cx) == cx and int(cy) == cy:
            point.add((int(cx), int(cy)))
# 최소 x, y값을 찾음
min_x, min_y = INF, INF
for x, y in point:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
diff_x = 0 - min_x
diff_y = 0 - min_y
# 원점으로 이동
zero_point = []
max_x, max_y = 0, 0
for x, y in point:
    zero_point.append([x + diff_x, y + diff_y])
    max_x = max(max_x, zero_point[-1][0])
    max_y = max(max_y, zero_point[-1][1])
# 반환 리스트 생성
star_arr = [list('.' * (max_x + 1)) for _ in range(max_y + 1)]
for x, y in zero_point:
    star_arr[max_y - y][x] = '*'
answer = []
for arr in star_arr:
    answer.append(''.join(arr))

print(answer)

#
# 반환 리스트 생성
# star_arr = [list('"' + '.' * (max_x + 1) + '"') for _ in range(max_y + 1)]
# for x, y in zero_point:
#     star_arr[max_y - y][x + 1] = '*'
# answer = []
# for arr in star_arr:
#     answer.append(''.join(arr))
