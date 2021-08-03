# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0
    payments = [i*price for i in range(1, count + 1)]
    total = sum(payments)
    if total > money:   answer = total - money
    return answer