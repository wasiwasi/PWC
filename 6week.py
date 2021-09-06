# 복서 정렬하기
weights = [145,92,86, 66]
head2head = ["NLWN","WNLN","LWNN", "NNNN"]
# [50,82,75,120] ["NLWL","WNLL","LWNW","WWLN"] [3,4,1,2]
# [145,92,86]	["NLW","WNL","LWN"]	[2,3,1]
# [60,70,60]	["NNN","NNN","NNN"]	[2,1,3]

heads = len(weights)
data = [[i + 1 , w] for i, w in enumerate(weights)]

for i, head in enumerate(head2head):
    matchCount = 0
    nCount = 0
    winCount = 0
    overweightCount = 0
    for j, h in enumerate(head):
        if h == 'W':
            matchCount += 1
            winCount += 1
            # 자신보다 무거운 복서라면 overweightCount 증가
            if data[i][1] < data[j][1]:
                overweightCount += 1
        elif h == 'L':
            matchCount += 1
        else:
            nCount += 1
    # 다른사람과 싸워본적이 없는 사람이라면
    if nCount == heads:
        data[i].append(0)
        data[i].append(0)
    else:
        data[i].append(winCount * 100 / matchCount)
        data[i].append(overweightCount)
data.sort(key = lambda x: (-x[2], -x[3], -x[1], x[0]))

print([x[0] for x in data])