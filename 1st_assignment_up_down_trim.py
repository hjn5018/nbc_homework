import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정


i = 1    # 시도 횟수 부여

i_list = []    # 시도한 횟수를 담을 리스트 생성

def max_tryout(i_list):     # 가장 큰 숫자 찾기(시도한 횟수 제일 큰 놈으로다가)
    max_num = i_list[0]
    for num in i_list:
        if num > max_num:
            max_num = num
    return max_num

print("<<업 다운 게임을 시작합니다.>>")    # 게임 시작

while True:    # 게임을 반복한다.(유저가 y 이외의 키를 입력하여 게임을 끝낼 때 까지)
    try:
        print(f'확인 용도 {random_number}')  # 무작위 숫자 확인 용도
        # i = 1    # 이건 실패의 흔적 (업이든 다운이든 분기가 끝나고 다시 while 돌면 횟수가 초기화 됨.)
        player_input = int(input("숫자를 입력하세요: "))  # player 입력 // str -> int
        if player_input > 100 or player_input < 1:  # 추가 도전 과제 1.
            print("1부터 100까지의 자연수를 입력해주세요!")  # 유효 범위 유도, 이건 횟수 안 세도록.
        else:
            if player_input > random_number:  # 숫자를 내리도록 유도.
                print("다운")
                i += 1  # 시도 횟수 증가.
            elif player_input < random_number:
                print("업")
                i += 1  # 시도 횟수 증가.
            else:  # player_input == random_number: 의 경우.
                print("정답입니다!")  # 정답임을 알려준다.
                print(f"시도한 횟수: {i}")  # f-string으로 시도횟수 i를 알려준다.
                i_list.append(i)  # '최고 시도 횟수'를 보여주기 위해 시도한 횟수를 i_list에 저장한다.
                regame = input("게임을 계속 하시겠습니까? (y/n): ")  # 추가 도전 과제 2.
                if regame == "y":  # 게임 재개
                    random_number = random.randint(1, 100)  # 새 게임 시작 전에 무작위 숫자 다시 한번 뽑기
                    i = 1  # 새 게임 시작 전에 시도 횟수 초기화
                else:
                    print(f"최고 시도 횟수는 {max_tryout(i_list)}회입니다.")  # 추가 도전 과제 3.
                    break  # 최고 시도 횟수 고지
    except: # 24번에서 거르지 못하는 소수, 문자열을 거른다.
        print("1부터 100까지의 자연수를 입력해주세요!")    # 오류 발생 시 안내.