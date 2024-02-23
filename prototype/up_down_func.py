# 함수 지향형으로 만들어보자!
import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정
print(random_number)

# i = 0 # UnboundLocalError: local variable 'i' referenced before assignment
        # 전역변수를 함수 내에서 돌리고 호출해서 그런 것 같은데.. 정확하게는..
# =================시도 횟수 출력 전=================================================================
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
# ================if문 함수로 쪼개기 전===================================================================
# def up_down():
#     i = 0
#     while True:
#         player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
#         if random_number > player_input:
#             i += 1
#             print("업")
#         elif random_number < player_input:
#             i += 1
#             print("다운")
#         else:
#             i +=1
#             print("정답입니다.")
#             print(f"시도한 횟수 : {i}")
#             break
# ===================================================================================

# up_down내에서 돌면서 늘어나는 횟수를 외부의 함수로 셀 수 있을까?
# ... 못 할 것 같은데
# player의 숫자가 범위를 벗어날 경우, 메시지를 출력하는 것도
# 따로 함수를 만들기는 힘들 것 같은데..
# =====================함수 쪼개기1(폐기)=======================================================
# def up_down():
#     i = 0
#     while True:
#         player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
#         comparison_num(player_input, i)
#         break


# def comparison_num(player_input, i):
#     if random_number > player_input:
#         i += 1
#         print("업")
#     elif random_number < player_input:
#         i += 1
#         print("다운")
#     else:
#         i += 1
#         print("정답입니다.")
#         print(f"시도한 횟수 : {i}")


#     elif random_number < player_input:
#                                      ^
    
# IndentationError: unindent does not match any outer indentation level
# 인덴트 해결 (복사 붙여넣기 하다보니 들여쓰기가 맞지 않았음[if문])
# SyntaxError: 'break' outside loop
# SyntaxError 해결 (break를 while문이 있는 함수로 옮겼음 // break야~ 앞으로는 길 잃어버리지 말거라~)
# NameError: name 'player_input' is not defined
# NameError 해결 (이게 고민이었는데 뭔말인지 알았음 ㅇㅇ 할거야)(comparison_num에서 변수가 두 갠데, random_number는 전역 변수라 괜찮은데, player_input이 정의되지 않았음. argument로 넣어줄게!)
# TypeError: comparison_num() missing 1 required positional argument: 'player_input'
# ㅇㅋㅇㅋ 뭔말인지 알겠어. comparison_sum에 기본값도 안 정해 놓은 argument 챙겨달라는거지? ㅇㅋㅇㅋ
# UnboundLocalError: local variable 'i' referenced before assignment
# i가 숨어있었구나? 기다려봐
# 아니 해달란대로 다 해줬더니 다 break를 걸어버리네
# ===================함수 쪼개기2(오류 생겨서 함수끼리의 순서 변경해봄)(폐기)=============================================================
# def comparison_num():
#     if random_number > player_input:
#             i += 1
#             print("업")
#         elif random_number < player_input:
#             i += 1
#             print("다운")
#         else:
#             i +=1
#             print("정답입니다.")
#             print(f"시도한 횟수 : {i}")
#             break

# def up_down():
#     i = 0
#     while True:
#         player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
#         comparison_num()
    # elif random_number < player_input:
    #                                  ^
# IndentationError: unindent does not match any outer indentation level
# ======================다시 함수 합치기ok//입력값 유도하기ok//리겜?? 이것도 break가 좀 걸리는데;;;;============================================================

# 순서 바꿔도 IndentationError 생기는 걸 보니
# comparison_num()에서 player_input를 직접 받지 않아서 생긴 문제인 것 같다.

# player 입력값 유도도 input에 따라 if문을 사용해야하니 따로 함수를 만들어서 사용하긴 힘들 것 같다.

def up_down():
    i = 0
    while True:
        player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
        if player_input > 100 or player_input < 1:
            print("1부터 100까지의 자연수를 입력해주세요.")
        else:
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

regame = input("게임을 계속 하시겠습니까? (y/n): ")
if regame == "y":
    random_number = random.randint(1, 100)   # 새 게임 시작 전에 무작위 숫자 다시 한번 뽑기
    i = 1 # 새 게임 시작 전에 시도 횟수 초기화
elif regame == "n":
# ========================함수에 입력값을 넣는 방법이 생각남(폐기)=======================================================

# def up_down():
#     i = 0
#     while True:
#         player_input = int(input("숫자를 입력하세요(1 ~ 100): "))
#         comparison_num(player_input)


# def comparison_num(player_input):    # 여기에 player input을 넣어보자
#     if random_number > player_input:
#             i += 1
#             print("업")
#         elif random_number < player_input:
#             i += 1
#             print("다운")
#         else:
#             i +=1
#             print("정답입니다.")
#             print(f"시도한 횟수 : {i}")
#             break

# IndentationError: unindent does not match any outer indentation level
    # 아!!!!!!!!!!!! 들여쓰기구나
# ======================================================================

up_down() # 업다운게임 호출(시작)
