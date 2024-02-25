# # 문제 1. 음수만 더해주세요
# # 새로운 리스트에 음수만 더해서 리스트를 출력해주세요
# """
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할_문장1
#     수행할_문장2
# """
# # 인덱싱 ㄴㄴ
#
#  # <<진용_문제1_답안>>
# ex1_list = [3223, 42, -3, 85, -238, 68, 12]
#
# negative_list = [] # 음수를 담을 빈 리스트 생성
#
# for i in ex1_list:
#     if i < 0:                 # 음수 분기점
#         negative_list.append(i)    # 빈 리스트에 음수만 저장
#
# print(negative_list)
# # [-3, -238]

# =======================================================================================

# """
# 문제 2
# 새로운 리스트에 kia, hyundai를 추가하라.
# """
#
# cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']
#
#
# # <<답안>>
# k_h_list = [] # kia와 hyundai만을 채울 빈 리스트를 생성합니다.
#
# for car in cars:
#     if car == 'kia' or car == 'hyundai': # car == 'kia'이거나 car == 'hyundai'인 경우에 다음 줄을 실행합니다.
#         k_h_list.append(car)             # 조건에 맞는 요소의 경우 빈 리스트에 추가합니다.('kia', 'hyundai')
#
# print(k_h_list)
# # ['kia', 'hyundai']                     # 요소를 돌면서 다음과 같은 과정이 발생합니다.
#                                          # if True or False -> if True (기아인 경우//append)
#                                          # if False or Ture -> if True (현대인 경우//append)
#                                          # if False or False -> if False (기아도 아니고 현대도 아닌 경우//실행 X)
# =======================================================================================
# """
# 문제 3
# 25 ~ -15까지 -2 감소하는 결과를 리스트로 출력해줘유
# range
#
# 결과 값
# [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15]
#
# range(start, stop, step)
#
# """
#
# # <<range 시험>>
# # for i in range(1, 3):
# #     print(i)
# #     # 1
# #     # 2
#
# # for i in range(3, 1):
# #     print(i)
# #     # 오류는 안 나는데, 출력이 없음.
# #     # range(3, 1, 1)의 경우도 마찬가지임
#
#
# # for i in range(3, 1, -1):
# #     print(i)
# #     # 3
# #     # 2
#
# # <<답안>>
# desc_list = []
# for i in range(25, -16, -2):
#     # print(i)
#     desc_list.append(i)
#
# print(desc_list)
# # [25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9, -11, -13, -15]

# =======================================================================================
#
# """
# 문제 4 Range advanced
# 1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력
#
# [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15]
# """

# <<답안>>
# def mul_10(num):       # 받은 인수에 10을 곱하는 함수입니다.
#     result = num * 10  # 짝수에 사용하려고 만들었습니다.
#     return result
#
# a_list = []            # range 요소를 저장하려고 만든 빈 리스트
#
# for i in range(1, 16):
#     if i % 2 == 0:             # 짝수면(나머지가 0이면)
#         result = mul_10(i)     # 10을 곱하는 함수에 인수로 넣고, 결과를 result 변수에 담는다.
#         a_list.append(result)
#     else:
#         a_list.append(i)
#
# print(a_list)
# # [1, 20, 3, 40, 5, 60, 7, 80, 9, 100, 11, 120, 13, 140, 15]

# =======================================================================================#
# 문제 5번?

# value 다 더해주세요(sum)

d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}

# <연습>

# for i in d:
#     print(i)
#     # a
#     # b
#     # c
#     # d
#     # e
#     # f
#     # g
#     # h

# for i, j in d:
#     print(i, j)
#     # ValueError: not enough values to unpack (expected 2, got 1)

# for i, j in d:
#     print((i, j))
#     # ValueError: not enough values to unpack (expected 2, got 1)

# for i, j in d:
#     print(f"{i}, {j}")
#     # ValueError: not enough values to unpack (expected 2, got 1)

# for i, j in d:
#     print(i)
#     print(j)
#     # ValueError: not enough values to unpack (expected 2, got 1)

# for i in d:
#     print(d[i])
#     # 15
#     # 634
#     # 124
#     # -436
#     # -235
#     # 856
#     # 23
#     # 523


# # <<답안>>
# empty_list = []

# for i in d:
#     empty_list.append(d[i])    # 딕셔너리의 밸류를 추출해서 빈 리스트에 담기. (리스트에서 합산하기 위함.)

# # print(empty_list)
# # # [15, 634, 124, -436, -235, 856, 23, 523]
    
# sum = 0

# for num in empty_list:
#     sum += num
#     # if num == empty_list[3]: # 합산이 제대로 이루어지고 있는지 검산([3]이면 4번째 요소까지 더한 값)
#     #     break

# print(sum)
# # 1504
# =======================================================================================
# # 문제 6번?

# """
# d = {'a': 'apple', 'b': 'banana'}
# d = {'a': 'apple', 'b': 'banana', 'c': 'kiwi', 'd' : 'grape'}
# 업데이트 해주세요~
# """

# <<답안>>
# d = {'a': 'apple', 'b': 'banana'}

# d['c'] = 'kiwi'

# # print(d)                                      # 'c'부터 잘 들어갔는지 확인
# # {'a': 'apple', 'b': 'banana', 'c': 'kiwi'}    # 확인 완료

# d['d'] = 'grape'

# # print(d)
# # {'a': 'apple', 'b': 'banana', 'c': 'kiwi', 'd': 'grape'}

# =======================================================================================
# # 문제 7번?
# """
# d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}

# value가 150 이상인 값만 더해주세유

# """


# <<답안>>
# d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}


# d_value = d.values() # value만을 담는 method이다.

# # print(d_value)
# # # dict_values([15, 634, 124, -436, -235, 856, 23, 523])

# sum = 0    # 여기에 150이상 값을 더해줍니다.

# # for i in d_value:
# #     print(i, end=" ")    # view 또한 list처럼 연산이 가능한지 확인해봅니다.
# #     # 15 634 124 -436 -235 856 23 523     # 확인 완료


# for i in d_value:
#     if i >= 150:
#         sum += i
#         # if i == d_value[0]:   # 검산용도 TypeError: 'dict_values' object is not subscriptable
#         #     break                   # => .value() method가 set-like object를 반환해서
#                                     # in같은 연산에는 적합해도, indexing에는 적합하지 않다고 한다.
#                                     # 만약에 indexing하고싶으면 list()로 감싸라고 한다.

# print(sum)
# # 2013


# # method를 list()로 감쌌을 경우
# # list_d_value = list(d_value)

# # # print(list_d_value)
# # # # [15, 634, 124, -436, -235, 856, 23, 523]
# =======================================================================================
"""
문제
해당 함수는 자연수 1개를 받음
1부터 해당 자연수까지 더하는 함수를 만드세요

자연수 10의 경우
결과 값 55

return 여부 비교
"""

# def sum(num):
#     sum_until_num = 0
#     for i in XXXX:          # 여기서 XXXX라는 리스트가 [1,2,3,4,5,...]처럼 무한하면 편리하겠다.
#         if i <= num:
#             sum_until_num += i
# -----------------------------------------------------------------------------------------------

# # <<답안>>
# def sum(num):
#     sum_num = 0
#     while True:
#         sum_num += num       # 이 순간 재귀함수가 있었으면 싶었다. 계속 1씩 빼면 되니까. 근데 사실은 while문이니까 계속 돌아감.
#         num -= 1   # num = 10이면 sum = 10, num = 9가 됨.
#         if num == 0:     # num = 0 인 순간에 sum은 1까지 다 더했음.
#             break        # while문 끝--->인데 왜 계속 돌아가지???? -> num -= num -1이 아니었습니다 ^^
#     print(sum_num)
#     # return sum_num     # return이라고 무한루프가 고쳐지진 않았음

# sum(10)
# # TypeError: sum() missing 1 required positional argument: 'num'

# # sum()
# # # TypeError: sum() missing 1 required positional argument: 'num'
# ----------------------------------------------------------------------------------------------

# 간단한 함수로 연습하기
# def hamsu():
#     print("나는 함수다")

# hamsu()
# # 나는 함수다
# --------------------------
# def hamsu1(num):
#     print(num)

# hamsu1(11)
# # 11
# # argument를 비웠다고 오류가 나진 않음.
# --------------------------
# def hamsu2(num):
#     sum = 0
#     while True:
#         sum += num
#         num -= 1        # 이 부분에서 num -= num - 1이 아니었구나;;;;;;
#         if num == 0:
#             break
#     print(sum)

# hamsu2(10)




# ========================================================================================
# =====================================질문=================================================
#
# 밑의 case2.에서 mul_10 함수는 return없이는 아무데도 쓰이지 못하는 건가요?


# # case1.
# # 함수에서 return할 경우
# def mul_10(num):       # 받은 인수에 10을 곱하는 함수입니다.
#     result = num * 10  # 짝수에 사용하려고 만들었습니다.
#     return result
#
# mul_10(12)
# # 오류는 없지만, 출력도 없다.
# # print(mul_10(12))
# # 잘 출력한다.

# =========================================================
#
# # case2.
# # 함수에서 return이 없을 경우
# def mul_10(num):
#     num * 10
#
# # mul_10(12)
# # 오류는 없지만, 출력도 없다.
#
# print(mul_10(12))
# # None
# # !!!!!!!!!!!! 왜 120이 아니지??????????
# # 그럼 여기서 함수부에 return을 넣는 수정이 없이
# # 120이 나오게 하려면 어떻게 하지????
# # GPT는 return을 쓰라고 한다.
# # 그럼 case2.의 함수는 return없이는 속 없는 강정인건가???