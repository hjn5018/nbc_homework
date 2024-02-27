class NanClass:
    # 클래스 변수 babgapt
    babgapt = 9000

        # 인스턴스 생성 시 자동으로 호출되는 함수(생성자)
    def __init__(self, chingoo):
        # 인스턴스 변수 self.chingoo
        self.chingoo = chingoo
        NanClass.babgapt += 10000

# 인스턴스 생성
freind1 = NanClass("돌정")

# 인스턴스 변수인 self.chingoo 참조
print(freind1.chingoo)
# babgapt을 참조할 때, 인스턴스 변수를 우선 탐색하고 일치하는 값이 없으면 클래스 변수 탐색
print(freind1.babgapt)
# ================================================
# class Account:
#         num_accounts = 0

#         def __init__(self, name):
#                 self.name = name

# kim = Account("kim")

# print(kim.name)


# ======================================================

# class Monster():
#     hp = 100

#     def damage(self, attack):
#         self.hp = self.hp - attack
# live = False

# m = Monster()
# m.damage(120)