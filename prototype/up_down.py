import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정


# if player_input == random_number: # 정답을 맞출 경우 "정답입니다!" 출력
#     print("정답입니다!")
# elif player_input > random_number: # 사용자 입력값이 정답보다 클 경우 "다운" 출력
#     print("다운")
# else: # 나머지 경우 "업" 출력
#     print("업")

i = 1 # 시도 횟수 부여

while True:
    print("<<업 다운 게임을 시작합니다.>>")
    print(random_number) # 무작위 숫자 확인 용도
    # i = 1
    player_input = int(input("숫자를 입력하세요: ")) # player 입력 // str -> int
    if player_input > 100 or player_input < 1:        # 추가 도전 과제 1.
        print("1부터 100까지의 자연수를 입력해주세요!")
    else:
        if player_input > random_number:
            print("다운")
            i += 1                                      # 오류입력을 세면 기분 나쁘니까 위치 조정
        elif player_input < random_number:
            print("업")
            i += 1
        else:                           # player_input == random_number: 의 경우입니다.
            print("정답입니다!")
            print(f"시도한 횟수: {i}")  # f string으로 시도횟수 i를 알려준다.
            regame = input("게임을 계속 하시겠습니까? (y/n): ")
            if regame == "y":
                random_number = random.randint(1, 100)   # 새 게임 시작 전에 무작위 숫자 다시 한번 뽑기
                i = 1 # 새 게임 시작 전에 시도 횟수 초기화
                
            elif regame == "n":
                break
            # else:
            #     print("y 또는 n을 입력해주세요") # 여기서 32nd line으로 돌아가고싶은데.......
#                 while True:
# NameError: name 'Ture' is not defined
# while True를 적으면 에러가 나오네..
            

# 풀이과정
# if문으로 골격 만들기(8th line ~ 13rd line)
# for문은 도저히 안 될 것 같아서, 아직 배우지 않은 while문 사용
# break는 떠올랐는데 continue가 떠오르지 않았음
# continue 떠오르고 적용했는데, 무한루프 발생(탈출 : Ctrl+C)
# continue 제외하고 break만 사용
    
# ==================================================================
#     **추가 도전 과제:**

# 1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요.
# 2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.
# 3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요.
    

# if player_input > 100 or player_input < 1:
#     print("1부터 100까지의 자연수를 입력해주세요!")
        
