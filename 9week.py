# 전력망을 둘로 나누기
n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
# 9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
# 4	[[1,2],[2,3],[3,4]]	0
# 7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
def find(chain, x):
    if x == chain[x]:
        return x

    chain[x] = find(chain, chain[x])
    return chain[x]

def union(chain, a, b):
    a = find(chain, a)
    b = find(chain, b)

    if a == b:
        return
    elif a < b:
        chain[b] = a
    elif a > b:
        chain[a] = b
        
def solution(n, wires):
    min_arr = []
    for i in range(n - 1):
        arr = wires[:i] + wires[i + 1:]
        # n = 2인경우
        if not arr:
            min_value = 0
            break

        chain = [k for k in range(n + 1)]
        
        for x, y in arr:
            union(chain, x, y)

        for k in range(1, n + 1): # 최종 갱신
            find(chain, k)

        one = chain.count(1)
        another = n - one

        min_arr.append(abs(one - another))

    print(min(min_arr))

solution(n, wires)
# INF = int(1e9)
# min_value = INF

# # 연결을 하나씩 끊으며 최소값을 찾음
# for i in range(n - 1):
#     arr = wires[:i] + wires[i + 1:]
#     # n = 2인경우
#     if not arr:
#         min_value = 0
#         break

#     chain = [INF] * (n + 1)
#     for x, y in arr:
#         # 새로운 전력망이라면
#         if chain[x] == INF and chain[y] == INF:
#             if min(chain) == INF:
#                 chain[x] = 0
#                 chain[y] = 0
#             else:
#                 chain[x] = min(chain) + 1
#                 chain[y] = min(chain) + 1
#         else:
#             chain[x] = min(chain[x], chain[y])
#             chain[y] = min(chain[x], chain[y])
    
#     # 0과 1로 나뉜 전력망의 내부 노드수를 카운트
#     zero = chain.count(0)
#     one = chain.count(1)

#     # 한 노드만 고립된 상태
#     if one == 0:
#         min_value = min(min_value, zero - 1)
#     else:
#         min_value = min(min_value, abs(zero - one))

# print(min_value)