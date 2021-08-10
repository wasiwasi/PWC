# 상호평가
score = [[100,90,98,88,65], [50,45,99,85,77], [47,88,95,80,67], [61,57,100,80,65], [24,90,94,75,65]]
n = len(score)
changed_score = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        changed_score[i][j] = score[j][i]
grade = []
for i in range(n):
    max_value = max(changed_score[i])
    min_value = min(changed_score[i])
    total_score = sum(changed_score[i])
    if max_value == changed_score[i][i] and changed_score[i].count(max_value) == 1:
        average = (total_score - max_value) // (n - 1)
    elif min_value == changed_score[i][i] and changed_score[i].count(min_value) == 1:
        average = (total_score - min_value) // (n - 1)
    else:
        average = total_score // n
    grade.append((lambda x: 'A' if average >= 90 else ('B' if average >= 80 else ('C' if average >= 70 else ('D' if average >= 50 else ('F')))))(average))
print(''.join(grade))