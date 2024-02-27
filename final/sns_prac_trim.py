from pprint import pprint
import hashlib

class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(self.name, self.username)


class Post():                            
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

member1 = Member('몰리1', '카다1', '보1')
member2 = Member('몰리2', '카다2', '보2')
member3 = Member('몰리3', '카다3', '보3')


members = []

member1_dict = {}
member1_dict["name"] = member1.name
member1_dict["username"] = member1.username
member1_dict["password"] = member1.password

member2_dict = {}
member2_dict["name"] = member2.name
member2_dict["username"] = member2.username
member2_dict["password"] = member2.password

member3_dict = {}
member3_dict["name"] = member3.name
member3_dict["username"] = member3.username
member3_dict["password"] = member3.password

members.append(member1_dict)
members.append(member2_dict)
members.append(member3_dict)

for member_dict in members:
    print(member_dict['name'])
# 몰리1
# 몰리2
# 몰리3


post1 = Post("오운완1", "오늘 운동 완료1", f"{member1.name}")
post2 = Post("오T완1", "오늘 TIL 완료1", f"{member1.name}")
post3 = Post("오S완1", "오늘 SQL 완료1", f"{member1.name}")
post4 = Post("오운완2", "오늘 운동 완료1", f"{member2.name}")
post5 = Post("오T완2", "오늘 TIL 완료1", f"{member2.name}")
post6 = Post("오S완2", "오늘 SQL 완료1", f"{member2.name}")
post7 = Post("오운완3", "오늘 운동 완료1", f"{member3.name}")
post8 = Post("오T완3", "오늘 TIL 완료1", f"{member3.name}")
post9 = Post("오S완3", "오늘 SQL 완료1", f"{member3.name}")

posts = []

post1_dict = {}
post1_dict["title"] = post1.title
post1_dict["content"] = post1.content
post1_dict["author"] = post1.author

post2_dict = {}
post2_dict["title"] = post2.title
post2_dict["content"] = post2.content
post2_dict["author"] = post2.author

post3_dict = {}
post3_dict["title"] = post3.title
post3_dict["content"] = post3.content
post3_dict["author"] = post3.author

post4_dict = {}
post4_dict["title"] = post4.title
post4_dict["content"] = post4.content
post4_dict["author"] = post4.author

post5_dict = {}
post5_dict["title"] = post5.title
post5_dict["content"] = post5.content
post5_dict["author"] = post5.author

post6_dict = {}
post6_dict["title"] = post6.title
post6_dict["content"] = post6.content
post6_dict["author"] = post6.author

post7_dict = {}
post7_dict["title"] = post7.title
post7_dict["content"] = post7.content
post7_dict["author"] = post7.author

post8_dict = {}
post8_dict["title"] = post8.title
post8_dict["content"] = post8.content
post8_dict["author"] = post8.author

post9_dict = {}
post9_dict["title"] = post9.title
post9_dict["content"] = post9.content
post9_dict["author"] = post9.author

posts.append(post1_dict)                  
posts.append(post2_dict)
posts.append(post3_dict)
posts.append(post4_dict)
posts.append(post5_dict)
posts.append(post6_dict)
posts.append(post7_dict)
posts.append(post8_dict)
posts.append(post9_dict)

for post in posts:                       
    if post['author'] == '몰리1':
        print(post['title'])

# # 오운완1
# # 오T완1
# # 오S완1

for post in posts:                        
    if '운동' in post['content']:
        print(post['title'])

# # 오운완1
# # 오운완2
# # 오운완3
        


print("<<회원가입을 환영합니다.>>")
print("=========================")
print("약관 : 안녕 hello")

create_instance_or_not = input("약관에 동의하십니까? (y/n): ") # Member 인스턴스 생성 준비

if create_instance_or_not == "y": # 약관에 동의하면
    member_a = Member(input("이름을 적어주세요: "), input("활동명을 적어주세요: "), input("비밀번호를 적어주세요: "))   # 인스턴스 생성

# =============================비밀번호 해싱==============================
iters = 100000    # 일반적인 반복 횟수
dk = hashlib.pbkdf2_hmac('sha256', b'member_a.password', b'madna', iters)
# brute-force attack을 대비한 pbkdf2_hmac
# madna라는 salt를 password에 섞어서 sha256으로 해싱한다.

member_a_dict = {}
member_a_dict["name"] = member_a.name
member_a_dict["username"] = member_a.username
member_a_dict["password"] = dk.hex()    # 비밀번호를 헥사값(16진법)으로 담는다.
# ===========================비밀번호 해싱 끝===============================
members.append(member_a_dict)    # 리스트에 인스턴스 정보 추가

pprint(members)


add_post = input("게시글을 작성하시겠습니까? (y/n): ")    # Post 인스턴스 생성 준비

if add_post == 'y':    # 동의하면
    post_a = Post(input("게시글의 제목을 지어주세요: "), input("내용을 적어주세요: "), f"{member_a.name}" )

posts = []    # post 인스턴스들의 정보를 담은 딕셔너리를 모아놓을 리스트 생성

post_a_dict = {}    # post 인스턴스의 정보를 담을 딕셔너리 생성
post_a_dict["title"] = post_a.title
post_a_dict["content"] = post_a.content
post_a_dict["author"] = post_a.author

posts.append(post_a_dict)    # 인스턴스의 딕셔너리를 리스트에 추가

pprint(posts)

# ===========================추가 도전 과제 .ver1 (input으로 사용자가 터미널에서 입력)=============================================

# print("<<회원가입을 환영합니다.>>")
# print("=========================")
# print("약관 : 안녕 hello")

# create_instance_or_not = input("약관에 동의하십니까? (y/n): ")

# if create_instance_or_not == "y": # 약관에 동의하면
#     member_a = Member(input("이름을 적어주세요: "), input("활동명을 적어주세요: "), input("비밀번호를 적어주세요: "))         # 인스턴스 생성

# member_a_dict = {}
# member_a_dict["name"] = member_a.name
# member_a_dict["username"] = member_a.username
# member_a_dict["password"] = member_a.password

# members.append(member_a_dict)

# # print(members)

# # -------------------post-----------------------------
# add_post = input("게시글을 작성하시겠습니까? (y/n): ")

# if add_post == 'y':
#     post_a = Post(input("게시글의 제목을 지어주세요: "), input("내용을 적어주세요: "), f"{member_a.name}" )

# post_a_dict = {}
# post_a_dict["title"] = post_a.title
# post_a_dict["content"] = post_a.content
# post_a_dict["author"] = post_a.author

# posts.append(post_a_dict)

# # print(posts)



# ===========================추가 도전 과제 .ver2 (비밀번호 해싱)=============================================

# from pprint import pprint    # 보기 좋게 출력하기
# import hashlib


# class Member():                          # 과제내용 1. Member 클래스 정의
#     name = ""                            # 과제내용 2. Member 클래스의 속성 name, username, password
#     username = ""
#     password = ""
#     def display(self):                   # 과제내용 3. Member 클래스의 메소드 // 회원정보를 출력하는 display(비밀번호 제외)
#         print(self.name, self.username)

# class Post():                            # 과제내용 1. Post 클래스 정의           
#     title = ""                           # 과제내용 4. Post 클래스의 속성 title, content, author(회원의 usename)
#     content = ""
#     author = "" 

# print("<<회원가입을 환영합니다.>>")
# print("=========================")
# print("약관 : 안녕 hello")

# create_instance_or_not = input("약관에 동의하십니까? (y/n): ") # Member 인스턴스 생성 준비

# if create_instance_or_not == "y": # 약관에 동의하면
#     member_a = Member(input("이름을 적어주세요: "), input("활동명을 적어주세요: "), input("비밀번호를 적어주세요: "))         # 인스턴스 생성

# # =============================비밀번호 해싱==============================
# iters = 100000    # 일반적인 반복 횟수
# dk = hashlib.pbkdf2_hmac('sha256', b'member_a.password', b'madna', iters)
# # brute-force attack을 대비한 pbkdf2_hmac
# # madna라는 salt를 password에 섞어서 sha256으로 해싱한다.

# member_a_dict = {}
# member_a_dict["name"] = member_a.name
# member_a_dict["username"] = member_a.username
# member_a_dict["password"] = dk.hex()    # 비밀번호를 헥사값(16진법)으로 담는다.
# # ========================================================================
# members.append(member_a_dict)    # 리스트에 인스턴스 정보 추가

# pprint(members)


# # -------------------post-----------------------------
# add_post = input("게시글을 작성하시겠습니까? (y/n): ")    # Post 인스턴스 생성 준비

# if add_post == 'y':    # 동의하면
#     post_a = Post(input("게시글의 제목을 지어주세요: "), input("내용을 적어주세요: "), f"{member_a.name}" )

# posts = []    # post 인스턴스들의 정보를 담은 딕셔너리를 모아놓을 리스트 생성

# post_a_dict = {}    # post 인스턴스의 정보를 담을 딕셔너리 생성
# post_a_dict["title"] = post_a.title
# post_a_dict["content"] = post_a.content
# post_a_dict["author"] = post_a.author

# posts.append(post_a_dict)    # 인스턴스의 딕셔너리를 리스트에 추가

# pprint(posts)

# # =======================================================================================================================
# # **추가 도전 과제:**

# # 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# # 2. post도 터미널에서 생성할 수 있게 해주세요.
# # 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

# # =======================================================================================================================
# # **평가**

# # - 클래스와 인스턴스 개념을 설명할 수 있는가?    클래스는 동일한 정보/기능을 가진 개체들을 생성하는 역할을 합니다.
# #                                              인스턴스는 클래스를 통해 만드는 개체입니다.
# # - 메소드와 어트리뷰트(속성)을 설명할 수 있는가? 어트리뷰트는 1차원적인 정보를 가지고, 이를 통해 각 인스턴스를 구분지을 수 있습니다.
# #                                              메소드는 인스턴스가 활용할 수 있는 기능입니다.
# # - 클래스를 정의할 수 있는가? 클래스는 속성과 메소드를 통해 인스턴스를 생성할 수 있습니다. 클래스에서 정의하는 함수를 메소드라고 부릅니다.
# #                            클래스를 파일로 저장하여 모듈의 기능으로 동작합니다. from 모듈 import 클래스
# # - 인스턴스를 생성할 수 있는가? '인스턴스이름 = 클래스이름()' 을 통하여 인스턴스를 생성할 수 있습니다.