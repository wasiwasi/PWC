k = 80
dungeons = [[80,20],[50,40],[30,10]]
# result = 3

def dfs(k, visited, dungeons):
    global count
    global max_value
    # 최대값 저장
    max_value = max(count, max_value)
    # 던전탐색
    for i, [need, consume] in enumerate(dungeons):
        # 방문한 던전은 패스
        if visited[i] == 1: continue
        # 갈 수 있는 던전이라면 방문함
        if k >= need and k - consume > 0:
            visited[i] = 1
            count += 1
            dfs(k - consume, visited, dungeons)
            count -= 1
            visited[i] = 0
    return

visited = [0] * len(dungeons)
max_value = 0
count = 0
dfs(k, visited, dungeons)
print(max_value)