import random

random_number = random.randint(1, 3) # 무작위 숫자 1, 2, 3 중 하나 생성(각각 가위, 바위, 보 지정할 거예요!)

# print(random_number) # 테스트 용도

computer_RCP = "" # 컴퓨터 가위바위보 빈 문자열

if random_number == 1:           # 무작위 1, 2, 3에 각각 가위, 바위, 보 지정
    computer_RCP = "가위" 
elif random_number == 2:
    computer_RCP = "바위"
else:                       # 3인 경우
    computer_RCP = "보"

# print(computer_RCP) # 테스트 용도
# ======================컴퓨터 가위바위보 생성 완료=========================
    
print("가위 바위 보 게임을 시작합니다!")

# print(player_input) # 테스트 용도
# =========================경우의 수=====================================
# if player_input == "가위":
#     if computer_RCP == "가위":
#         print("비겼습니다.")
#     elif computer_RCP == "바위":
#         print("졌습니다..")
#     else:                         # computer__input == "보" 인 경우
#         print("이겼습니다!")
# elif player_input == "바위":
#     if computer_RCP == "가위":
#         print("이겼습니다!")
#     elif computer_RCP == "바위":
#         print("비겼습니다.")
#     else:
#         print("졌습니다..")
# else:                             # player_input == "보" 인 경우
#     if computer_RCP == "가위":
#         print("졌습니다..")
#     elif computer_RCP == "바위":
#         print("이겼습니다!")
#     else:
#         print("비겼습니다.")
# =========================경우의 수=====================================
records = [] # 게임 승무패 기록 저장하기위한 빈 리스트 생성

def winlosedraw(list):                      # 승무패 기록 출력 함수 .ver2(인덴트 수정 win_num부터 print()까지)
    win_list = []
    lose_list = []
    draw_list = []
    for i in list:
        if i == "승":
            win_list.append(i)
        elif i == "패":
            lose_list.append(i)
        else:
            draw_list.append(i)

    win_num = len(win_list)
    lose_num = len(lose_list)
    draw_num = len(draw_list)

    print(f"승 : {win_num}, 패 : {lose_num}, 무승부 : {draw_num}")

while True:
    player_input = input("안 내면 진거 가위 바위 보!: ")  # player가 가위, 바위, 보 중 하나를 입력한다.

    if player_input == "가위":        # 이 구문이 어지러워 보여서 def를 쓸까 했는데, 분기마다 내용이 달라져서 정의하기 어려울 것 같다.
        if computer_RCP == "가위":    
            records.append("무")      # 게임 결과 records 리스트에 기록하기
            print("비겼습니다.")       # 비긴 경우 player에게 알려주기
        elif computer_RCP == "바위":
            records.append("패")
            print("졌습니다..")        # player가 진 경우 player에게 알려주기
        else:                         # computer__input == "보" 인 경우
            records.append("승")
            print("이겼습니다!")       # player가 이긴 경우 player에게 알려주기
    elif player_input == "바위":
        if computer_RCP == "가위":
            records.append("승")
            print("이겼습니다!")
        elif computer_RCP == "바위":
            records.append("무")
            print("비겼습니다.")
        else:
            records.append("패")
            print("졌습니다..")
    elif player_input == "보":            # player_input == "보" 인 경우                 
        if computer_RCP == "가위":
            records.append("패")
            print("졌습니다..")
        elif computer_RCP == "바위":
            records.append("승")
            print("이겼습니다!")
        else:
            records.append("무")
            print("비겼습니다.")
    else:
        print("유효한 입력이 아닙니다.")      # 원래는 player_input == "보"인 경우를 else로 했는데
                                            # else에 오타입력일 때에도 들어가버려서 게임할 때 좀 억울했음
                                            # append하지 않으면 괜찮으니까 조금 번거롭더라도 elif 하나 생성하고 else따로 빼줌

    ask_more = input("한 판 더? (y/n): ")  # 게임 반복 또는 종료
    if ask_more == "y" or ask_more == "Y": # 대소문자 구분하지 않도록 -- 추가도전과제 2.
        continue
    else:                                 # 솔직히 게임하고 싶은 사람만 y 누르지
        winlosedraw(records)              # 그만하고 싶으면 정확히 n을 누르지 않아도 되지 않을까?
        
        # 승 : 1, 패 : 0, 무승부 : 0
        # 승 : 1, 패 : 1, 무승부 : 0
        # 승 : 1, 패 : 1, 무승부 : 1
        # 승 : 2, 패 : 1, 무승부 : 1
        # 이게 반복이 되네;;
        # TypeError: winlosedraw() missing 1 required positional argument: 'list'
        # 리스트(records)를 인수로 넣자!
        # print(records)              # 게임 기록 저장 확인 완료
        # print(f"전적 : {}")          # player에게 게임 기록 알려주기 // {}에 변수 넣어야함!!
        break

# ===============================================================================================
# 풀이과정
# 가위바위보를 하긴 해야하니까
# 1. 컴퓨터도 주먹을 쥐어준다.
# 2. 계속 주먹만 내면 안되니까 무작위로 해야한다.
# 3. 내가 아는 무작위는 random이니까 import하고 randint(1, 3) 해준다
# 4. (1, 가위), (2, 바위), (3, 보)로 연결해준다.
# 5. 플레이어는 input을 받아서 처리해야하니까 if문으로 갈래를 만들어야한다.
# 6. 가위의 경우 가위바위보, 바위의 경우 가위바위보, 보의 경우 가위바위보를 생성한다.
# 7. 각 사건마다 승,무,패를 알려준다.
# 8. if문은 처리했고, 반복문을 넣어야 하는데..
#    여기서도 for문은 힘들 것 같아서 while을 적용한다.
# 9. 반복or종료 여부를 묻고(input)(y/n) continue와 break로 마감한다. 
# 10. 승무패 기록 만들기 (빈 리스트, 분기마다 append, 함수로 승무패 각각의 리스트 생성[for문 append, len()])
# ================================================================================
#     **추가 도전 과제:**

# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요. ok
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요. ok
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요. 추가도전이 아니더라도 기본과제와 겹치지 않은가요?
                                                                                                                #  기본과제 : '게임을 반복하거나 종료할 수 있는 기능을 추가하세요.' 


# ================================================================================

# 승무패 기록 저장하고
# (승 : x 패 : y 무승부 : z)로 나타내려면??
# 일단 append했으니까 그거부터 확인하자. -> 확인 완료(else문에서 print(records))
    
# 이제 list에서 승무패를 갈라야하는데 if문??
# =======================================================================================
# def winlosedraw(list):                      # 승무패 기록 출력 함수 .ver1
#     win_list = []
#     lose_list = []
#     draw_list = []
#     for i in list:
#         if i == "승":
#             win_list.append(i)
#         elif i == "패":
#             lose_list.append(i)
#         else:
#             draw_list.append(i)

#         win_num = len(win_list)
#         lose_num = len(lose_list)
#         draw_num = len(draw_list)

#         print(f"승 : {win_num}, 패 : {lose_num}, 무승부 : {draw_num}")

# 인덴트 때문에 for문에 print가 들어가버렸네;;
# ===========================================================================================
# def winlosedraw(list):                      # 승무패 기록 출력 함수 .ver2(인덴트 수정 win_num부터 print()까지)
#     win_list = []
#     lose_list = []
#     draw_list = []
#     for i in list:
#         if i == "승":
#             win_list.append(i)
#         elif i == "패":
#             lose_list.append(i)
#         else:
#             draw_list.append(i)

#     win_num = len(win_list)
#     lose_num = len(lose_list)
#     draw_num = len(draw_list)

#     print(f"승 : {win_num}, 패 : {lose_num}, 무승부 : {draw_num}")
# 잘 되네 ^^
    
# 평가==================================================================

# - 사용자의 입력값을 ‘가위 바위 보’로 제한할 수 있는가 ok --->append()달지 않고, else: print("유효한 입력이 아닙니다.")
# - 컴퓨터가 랜덤으로 ‘가위 바위 보’를 선택하게 할 수 있는가 ok --> random.randint(1,3)을 각각 배정
# - 다중 if 문으로 승패를 비교할 수 있는가 ok
# - while문을 이용해서 경기를 반복시키고 통계를 만들 수 있는가 ok --> 빈 리스트에 저장하고 def만들어서 각각 리스트에 분류하고, len()