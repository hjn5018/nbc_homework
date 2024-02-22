import random

random_number = random.randint(1, 3) # 무작위 숫자 1, 2, 3 중 하나 생성

# print(random_number) # 테스트 용도

computer_RCP = "" # 컴퓨터 가위바위보 빈 문자열

if random_number == 1:
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
#     else:
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
    player_input = input("안 내면 진거 가위 바위 보!: ")

    if player_input == "가위":
        if computer_RCP == "가위":
            print("비겼습니다.")
        elif computer_RCP == "바위":
            print("졌습니다..")
        else:
            print("이겼습니다!")
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

    ask_more = input("한 판 더? (y/n): ")
    if ask_more == "y":
        continue
    else:
        break
