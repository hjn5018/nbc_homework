import random

random_number = random.randint(1, 100) # 1 ~ 100 무작위 숫자 선정


# if player_input == random_number: # 정답을 맞출 경우 "정답입니다!" 출력
#     print("정답입니다!")
# elif player_input > random_number: # 사용자 입력값이 정답보다 클 경우 "다운" 출력
#     print("다운")
# else: # 나머지 경우 "업" 출력
#     print("업")
# ===============================================================================================
i = 1 # 시도 횟수 부여
i_list = []

def max_tryout(i_list):
    max_num = i_list[0]
    for num in i_list:
        if num > max_num:
            max_num = num
    return max_num

print("<<업 다운 게임을 시작합니다.>>")

while True:
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
            i_list.append(i) # 시도한 횟수를 빈 리스트(i_list)에 저장하자!
            regame = input("게임을 계속 하시겠습니까? (y/n): ")
            if regame == "y":
                random_number = random.randint(1, 100)   # 새 게임 시작 전에 무작위 숫자 다시 한번 뽑기
                i = 1 # 새 게임 시작 전에 시도 횟수 초기화
            elif regame == "n":
                print(f"최고 시도 횟수는 {max_tryout(i_list)}회입니다.")
                break
# ============================================================================================================



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

# if player_input > 100 or player_input < 1:
#     print("1부터 100까지의 자연수를 입력해주세요!")
'''
1. 프로그램은 다음과 같은 기능을 포함해야 합니다.
    - 컴퓨터는 1부터 100 사이의 랜덤한 숫자를 생성합니다. ok
    - 플레이어는 숫자를 입력하고, 입력한 숫자와 컴퓨터의 숫자를 비교하여 "업" 또는 "다운" 힌트를 제공합니다. ok
    - 플레이어가 컴퓨터의 숫자를 정확히 맞히면 시도한 횟수를 알려줍니다. ok
    - 플레이어가 숫자를 맞힐 때까지 위 과정을 반복합니다. ok

**추가 도전 과제:**

1. 플레이어가 입력한 숫자가 범위를 벗어날 경우, 적절한 안내 메시지를 출력하여 유효한 범위 내의 숫자를 입력하도록 유도하세요. ok
2. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요. ok
3. 게임이 종료될 때 플레이어의 최고 시도 횟수를 기록하고, 다음 게임에서 이를 표시하는 기능을 구현하세요. not ok
                                                                                                게임이 좋료될 때가 언제인가
                                                                                                y->5 y->3 y->7 y... n했을 때가 종료라면?
                                                                                                잘 모르겠지만 35th line이 문제인듯
'''


'''
35th line의 i=1이 되기 전에 i를 j에 담아서 어떻게 처리해야하는데
y해서 게임이 또 시작되고 i가 내려오면 j도 초기화된단말이지..
j를 대피시켜야하는데..
sql이면 max든 뭐든 쓸텐데..

그럼 아예 i=1로 초기화하는 위치를 변경하면?..
크흠..
어쨋건
i=5가 내려오고
i=7이 내려오고
i=1이 내려오든 n으로 출력하는 건 마지막 값이 되어버리는데..

일단 초기화를 안 한다고 가정하고 while을 돈다고 해보자.
그러면 그대로 숫자가 계속 더해진다. aosidfhiashdf
초기화를 하긴 해야하는데..
기록을 저장하긴 해야하는데..
while 바로 앞에 i=1 해버리면 100이상 1이하 입력했을 때 초기화가 되어버리니까 안되고,
어쩔 수 없이 35th line에 둬야겠고.
그렇다면 저장이 문젠데..
j에 i를 저장하고 글로벌 선언을 해버리면..??
잘 모르겠는데?
???????????????????????????????????????????????????????
된 것 같은데????
아니네
그럴리가 없지 ^^

dk!!!!!!!!!!!!!!!!!!!11111
빈 리스트 하나 만들고, i를 받아서 계속 append하고 max 출력하면 되는 거 아닌가?
물론 max는 없으니까 for문 돌려야겠지만

일단
리스트 쌓아두고, n한 순간에 거기서 최대값 뽑아야할거야
그럼 거기서 max_tryout()으로
최대값 뽑고
거기 return값을 f-string에 넣으면 되겠네?

그럼 max_tryout()부터 만들어볼까

근데 아직 로직을 모르잖아..

'''

# =========================================================================================
# 로직 만들어보자

# ex_list = [45, 7, 15, 9, 82, 70, 30, 20]

# 최대값은 82다. return도 82 해야한다.

# for i in ex_list:
#     if i > ex_list(i + 1):
#         print(i)
#         무슨 말인지 알지?? 근데 이거 아닌 거 알지?? enumerate 써보자(7시 세션에서 경원튜터님 말씀이 생각났음) class라고 하니까 import 해야하려나.......... 일단 그냥 해보자

# asdf = enumerate(ex_list, 1)
# 아.. 어떻게 소환한담..

# TIL보고 왔습니다.

# for i, j in enumerate(ex_list):
#     print(i, j)
#     print(j)
#     print(i)
#     막막하네..
#     구현부 봐도 모르겠네
#     배운거긴 한데..
#     배웠을 때도 오래 걸렸구나..
#     심지어 enumerate도 안 쓰네

# ex_list = [45, 7, 15, 9, 82, 70, 30, 20]

# max_num = ex_list[0]

# for num in ex_list:
#     if num > max_num:
#         max_num = num

# result = max_num

# print(result)

