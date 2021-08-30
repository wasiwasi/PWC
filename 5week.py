# 모음 사전
from itertools import product
word = "AAAE" # expect 10
print(sorted(sum([list(product("AEIOU", repeat = i)) for i in range(1, 6)], [])).index(tuple(word)) + 1)

"""
pruduct의 repeat, sum 의 기본값을 배열로 줄 시 배열연산 가능
"""

# 초안
# mydict = []
# for i in range(1, 6):
#     mydict.extend(list(product("AEIOU", repeat = i)))
# print(sorted(mydict).index(tuple(word)) + 1)