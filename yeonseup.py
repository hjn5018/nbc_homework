"""
문제 2
새로운 리스트에 kia, hyundai를 추가하라.
"""

cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']



"""
문제 3
25 ~ -15까지 -2 감소하는 결과를 리스트로 출력해줘유
range

결과 값
[25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15]

range(start, stop, step)

"""




"""
문제 4 Range advanced
1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력

[1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15]
"""
def mul_10(num):
    result = num * 10
    return result

a_list = []

for i in range(1, 16):
    if i % 2 == 0:
        result = mul_10(i)
        a_list.append(result)
    else:
        a_list.append(i)
    
print(a_list)
# =================================================================