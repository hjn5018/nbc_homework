import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정
print(random_number) # 테스트 용도

print("<<업 다운 게임을 시작합니다.>>")

# if player_input == random_number: # 정답을 맞출 경우 "정답입니다!" 출력
#     print("정답입니다!")
# elif player_input > random_number: # 사용자 입력값이 정답보다 클 경우 "다운" 출력
#     print("다운")
# else: # 나머지 경우 "업" 출력
#     print("업")

i = 1 # 게임 시행 횟수

while True:
    i += 1
    player_input = int(input("숫자를 입력하세요: ")) # player 입력 // str -> int
    
    if player_input > random_number:
        print("다운")
        
    elif player_input < random_number:
        print("업")
        
    else:
        print("정답입니다.")
        print(f"시도한 횟수: {i}")
        break

# 풀이과정
# if문으로 골격 만들기(8th line ~ 13rd line)
# for문은 도저히 안 될 것 같아서, 아직 배우지 않은 while문 사용
# break는 떠올랐는데 continue가 떠오르지 않았음
# continue 떠오르고 적용했는데, 무한루프 발생(탈출 : Ctrl+C)
# continue 제외하고 break만 사용