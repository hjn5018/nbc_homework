# 함수 지향형으로 만들어보자!
import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정
print(random_number)

# i = 0 # UnboundLocalError: local variable 'i' referenced before assignment
        # 전역변수를 함수 내에서 돌리고 호출해서 그런 것 같은데.. 정확하게는..

# def up_down():
#     while True:
#         player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
#         if random_number > player_input:
#             print("업")
#         elif random_number < player_input:
#             print("다운")
#         else:
#             print("정답입니다.")
#             break

def up_down():
    i = 0
    while True:
        player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
        if random_number > player_input:
            i += 1
            print("업")
        elif random_number < player_input:
            i += 1
            print("다운")
        else:
            i +=1
            print("정답입니다.")
            print(f"시도한 횟수 : {i}")
            break


up_down() # 업다운게임 호출(시작)

# up_down내에서 돌면서 늘어나는 횟수를 외부의 함수로 셀 수 있을까?... 못 할 것 같은데

