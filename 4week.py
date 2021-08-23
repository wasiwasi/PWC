# 직업군 추천하기
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]
new_table = [occupation.split()[::-1] for occupation in table]
max_value = 0
for occupation in new_table:
    sum = 0
    for i, language in enumerate(languages):
        if language in occupation:
            sum += (occupation.index(language) + 1) * preference[i]
    if sum > max_value:
        max_value = sum
        answer = occupation[-1]
    elif sum == max_value:
        answer = min(occupation[-1], answer)
print(answer)