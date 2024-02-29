import random


# player_input = input()

# print(player_input)

# print(player_input.isdigit())
# # 4 -> True
# # r -> False
# # 1.1 -> False

random_number = random.randint(1, 100)
player_input = input("숫자를 입력하세요 : ")
# while player_input.isdigit():
#     if player_input > random_number:
#         print("다운")
#     elif player_input < random_number:
#         print("업")
#     else:
#         print("정답입니다.")









def right_answer_or_not():
    
    print(f'테스트 중입니다 : {random_number}')
    

    if player_input != random_number:
        
    else:
        print("정답입니다.")
        input("다시 시도하시겠습니까? (y/n)")




def up_or_down():
    if player_input > random_number:
        print("다운")
    else:
        print("업")