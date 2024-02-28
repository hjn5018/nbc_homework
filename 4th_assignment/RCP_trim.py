import random

random_number = random.randint(1, 3) # 무작위 숫자 1, 2, 3 중 하나 생성(각각 가위, 바위, 보 지정할 거예요!)


computer_RCP = "" # 컴퓨터 가위바위보 빈 문자열

if random_number == 1:           # 'random_number'에 담길 숫자 1, 2, 3에 각각 가위, 바위, 보 지정
    computer_RCP = "가위"
elif random_number == 2:
    computer_RCP = "바위"
else:                       # 'random_number == 3'인 경우
    computer_RCP = "보"


print("가위 바위 보 게임을 시작합니다!")    # 게임 시작

records = []  # 게임 승무패 기록 저장하기위한 빈 리스트 생성


def winlosedraw(list):  # 승무패 기록 출력 함수 .ver2(인덴트 수정 win_num부터 print()까지)
    win_list = []  # 이긴 기록 저장할 빈 리스트
    lose_list = []  # 진 기록 저장할 빈 리스트
    draw_list = []  # 비긴 기록 저장할 빈 리스트
    for i in list:
        if i == "승":
            win_list.append(i)  # 이긴 경우 win_list에 추가
        elif i == "패":
            lose_list.append(i)  # 진 경우 lose_list에 추가
        else:
            draw_list.append(i)  # 비긴 경우 draw_list에 추가

    win_num = len(win_list)  # 각 경우의 개수를 센다.
    lose_num = len(lose_list)
    draw_num = len(draw_list)

    print(f"승 : {win_num}, 패 : {lose_num}, 무승부 : {draw_num}")  # 게임의 승무패 기록을 보여준다.

def gamestart():
    while True:
        player_input = input("안 내면 진 거 가위 바위 보!: ")  # player가 가위, 바위, 보 중 하나를 입력한다.

        if player_input == "가위":  # 이 구문이 어지러워 보여서 def를 쓸까 했는데, 분기마다 내용이 달라져서 정의하기 어려울 것 같다.
            if computer_RCP == "가위":
                records.append("무")  # 게임 결과 records 리스트에 기록하기
                print("비겼습니다.")  # 비긴 경우 player에게 알려주기
            elif computer_RCP == "바위":
                records.append("패")
                print("졌습니다..")  # player가 진 경우 player에게 알려주기
            else:  # computer__input == "보" 인 경우
                records.append("승")
                print("이겼습니다!")  # player가 이긴 경우 player에게 알려주기
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
        elif player_input == "보":  # player_input == "보" 인 경우
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
            print("유효한 입력이 아닙니다.")  # 원래는 player_input == "보"인 경우를 else로 했다.
            # 시험삼아서 게임했을 때, else에 오타입력일 때에도 들어가버려서 게임할 때 좀 억울했음
            # append하지 않으면 괜찮으니까 조금 번거롭더라도 elif 하나 생성하고 else따로 빼줌
            continue
        ask_more = input("한 판 더? (y/n): ")  # 게임 반복 또는 종료
        if ask_more == "y" or ask_more == "Y":  # 대소문자 구분하지 않도록 -- 추가도전과제 2.
            continue
        else:  # 솔직히 게임하고 싶은 사람만 y 누르니까,
            winlosedraw(records)  # 그만하고 싶으면 정확히 n을 누르지 않아도 되지 않을까?

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

gamestart()