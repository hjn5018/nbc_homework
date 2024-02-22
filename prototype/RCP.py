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

while True:
    player_input = input("안 내면 진거 가위 바위 보!: ")  # player가 가위, 바위, 보 중 하나를 입력한다.

    if player_input == "가위":
        if computer_RCP == "가위":
            print("비겼습니다.")       # 비긴 경우 player에게 알려주기
        elif computer_RCP == "바위":
            print("졌습니다..")        # player가 진 경우 player에게 알려주기
        else:                         # computer__input == "보" 인 경우
            print("이겼습니다!")       # player가 이긴 경우 player에게 알려주기
    elif player_input == "바위":
        if computer_RCP == "가위":
            print("이겼습니다!")
        elif computer_RCP == "바위":
            print("비겼습니다.")
        else:
            print("졌습니다..")
    else:                             # player_input == "보" 인 경우
        if computer_RCP == "가위":
            print("졌습니다..")
        elif computer_RCP == "바위":
            print("이겼습니다!")
        else:
            print("비겼습니다.")

    ask_more = input("한 판 더? (y/n): ")  # 게임 반복 또는 종료
    if ask_more == "y":
        continue
    else:
        break


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
# =========================================================
#     **추가 도전 과제:**

# 1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요.
# 2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요.
# 3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
