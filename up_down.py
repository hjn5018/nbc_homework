import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정
print(random_number)

player_input = input() # 사용자 입력

# if player_input > random_number:
#     print("다운")
# else:
#     print("ㄱㄷㄱㄷ")
#     # TypeError: '>' not supported between instances of 'str' and 'int'

player_input = int(player_input) # 사용자 입력값 int로 변환

if player_input == random_number: # 정답을 맞출 경우 "정답입니다!" 출력
    print("정답입니다!")
elif player_input > random_number: # 사용자 입력값이 정답보다 클 경우 "다운" 출력
    print("다운")
else: # 나머지 경우 "업" 출력
    print("업")

while player_input != random_number: