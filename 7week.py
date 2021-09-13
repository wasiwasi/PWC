# 입실 퇴실
enter = [1,4,2,3]	
leave = [2,1,4,3]	
# [1,4,2,3] [2,1,3,4] [2,2,1,3]
# [1,4,2,3]	[2,1,4,3] [2,2,0,2]

length = len(enter)
answer = [0] * (length + 1)
# 현재 입실해 있는 인원
room = []
# enter의 어디까지 진행했는지를 저장하기위한 인덱스
entered_point = 0
for leaver in leave:
    # 떠날사람이 이미 방에 있다면 삭제
    if leaver in room:
        room.remove(leaver)
        continue
    # 떠나야 하는 사람이 방안에 없다면 그 사람이 들어올때 까지 사람을 넣음
    leaver_index = enter.index(leaver)
    for i in range(entered_point, leaver_index + 1):
        # 들어온 사람은 방안에 있는 사람 수 만큼 정답카운트증가
        answer[enter[i]] += len(room)
        # 사람이 들어오면 방안에 있는 사람들은 1만큼 카운트증가
        for r in room:
            answer[r] += 1
        # 새로들어온 사람 추가
        room.append(enter[i])
    # 마지막에 들어온 사람은 leaver와 같음 따라서 pop
    room.pop()
    # 다음 시작인덱스를 저장
    entered_point = leaver_index + 1

print(answer[1:])