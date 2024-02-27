from pprint import pprint

class NanClass:
    # 클래스 변수 babgapt
    babgapt = 9000

        # 인스턴스 생성 시 자동으로 호출되는 함수(생성자)
    def __init__(self, chingoo):
        # 인스턴스 변수 self.chingoo
        self.chingoo = chingoo
        NanClass.babgapt += 10000

# 인스턴스 생성
friend1 = NanClass("돌정")
print(friend1.babgapt)
# 19000
friend2 = NanClass("노노")

# 인스턴스 변수인 self.chingoo 참조
print(friend1.chingoo)
# 돌정

# babgapt을 참조할 때, 인스턴스 변수를 우선 탐색하고 일치하는 값이 없으면 클래스 변수 탐색
# print(friend1.babgapt)
# 19000

print(friend2.babgapt)
# 29000
# =========================================================================


# print(dir())
# #['NanClass', '__annotations__', '__builtins__', '__cached__', '__doc__',
# # '__file__', '__loader__', '__name__', '__package__', '__spec__', 'freind1']

# # 기존 directory에서 정의한 클래스(NanClass)와 생성한 인스턴스(freind1)가 추가되었다. 
# # --> dir에 있기 때문에 편집기에 아무 이유 없이 그냥 입력해도 오류표시 나지 않음



# pprint(NanClass.__dict__)
# # mappingproxy({'__dict__': <attribute '__dict__' of 'NanClass' objects>,
# #               '__doc__': None,
# #               '__init__': <function NanClass.__init__ at 0x00000281B432A820>,
# #               '__module__': '__main__',
# #               '__weakref__': <attribute '__weakref__' of 'NanClass' objects>,
# #               'babgapt': 9000})

# # 파이썬에서는 클래스가 정의되면 독립적인 네임스페이스가 생성된다.
# # __dict__속성으로 네임스페이스를 확인할 수 있다.
# # NanClass에서 정의한 __init__함수와 'babgapt':9000 키,밸류를 확인할 수 있다.


# # 네임스페이스에 저장된 변수나 메서드를 통해 값에 접근할 수 있다.
# print(friend1.chingoo)
# # 돌정
# print(friend1.babgapt)
# # 19000


# # 인스턴스(friend1)의 네임스페이스
# print(friend1.__dict__)
# # {'chingoo': '돌정'}

# print(friend1)
# # <__main__.NanClass object at 0x0000027E03818B50>
# # __main__은 NanClass의 네임스페이스 중 __modle__에 대응하는 값이다.

# =====================================================

# 네임스페이스란?
# 변수와 객체의 관계를 저장하는 공간

# (변수) a = 2 (객체)
# 의 관계를 저장한다.

