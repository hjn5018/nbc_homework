# def aguu(*args):
#     print(*args)

# aguu("에구구", "구름", "메르")
# 에구구 구름 메르

# def aguu(*args):
#     print(args)

# aguu("에구구", "구름", "메르")
# # ('에구구', '구름', '메르')

# def aguu(**kwargs):
#     print(**kwargs)

# aguu(에구구 = "에궁")
# # TypeError: '에구구' is an invalid keyword argument for print()

# def aguu(**kwargs):
#     print(*kwargs)

# aguu(에구구 = "에궁")
# # 에구구

# def aguu(**kwargs):
#     print(kwargs)

# aguu(에구구 = "에궁")
# # {'에구구': '에궁'}

# def aguu(**kwargs):
#     print(kwargs)

# aguu(에구구 = "에궁", 구름 = "치즈", 메르 = "루시드")
# # {'에구구': '에궁', '구름': '치즈', '메르': '루시드'}

# def aguu(**kwargs):
#     print(*kwargs)

# aguu(에구구 = "에궁", 구름 = "치즈", 메르 = "루시드")
# # 에구구 구름 메르


# class Member:
#     def __init__(self, **kwargs):
#         self.name = kwargs[name]
#         self.username = kwargs[username]
#         self.password = kwargs[password]

# m1 = Member("도노반", "Mr.70", 70)
# # TypeError: __init__() takes 1 positional argument but 4 were given

# class Member:
#     def __init__(self, name, username, password):
#         self.name = name
#         self.username = username
#         self.password = password

# m1 = Member("도노반", "Mr.70", 70)
# # TypeError: __init__() takes 1 positional argument but 4 were given

# # print(m1)
# # # <__main__.Member object at 0x000001874AADA790>

# # print(m1.name)
# # # 도노반

# # print(m1.name, m1.username)
# # # 도노반 Mr.70


# user_dict = {}

# class Member:

#     def __init__(self, name, username, password):
#         self.name = name
#         self.username = username
#         self.password = password
#         # user_list.append(name)
#         user_dict[name] = self.name
#         # print(self.name, self.username)
#     def user_info(self):
#         print(self.name, self.username)


# m1 = Member("도노반", "Mr.70", 70)
# m2 = Member("스코티", "by", "rapgod")
# m3 = Member("불곰", "콜라", "주세요")

# # m1.user_info()
# # # 도노반 Mr.70

# print(user_dict)
# {'name': '불곰'}

user_list = []
user_dict = {}

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        # user_list.append(name)
        # print(self.name, self.username)
    def user_info(self):
        print(self.name, self.username)


m1 = Member("도노반", "Mr.70", 70)
m2 = Member("스코티", "by", "rapgod")
m3 = Member("불곰", "콜라", "주세요")

# m1.user_info()
# # 도노반 Mr.70

# print(user_dict)
# # {'도노반': '도노반', '스코티': '스코티', '불곰': '불곰'}
