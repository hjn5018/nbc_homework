from pprint import pprint

class Member():                          # 과제내용 1. Member 클래스 정의
    name = ""                            # 과제내용 2. Member 클래스의 속성 name, username, password
    username = ""
    password = ""
    def display(self):                   # 과제내용 3. Member 클래스의 메소드 // 회원정보를 출력하는 display(비밀번호 제외)
        print(self.name, self.username)

class Post():                            # 과제내용 1. Post 클래스 정의           
    title = ""                           # 과제내용 4. Post 클래스의 속성 title, content, author(회원의 usename)
    content = ""
    author = "" 

member1 = Member()                       # 과제내용 5. 회원 인스턴스 세 개 이상 생성
member2 = Member()
member3 = Member()

member1.name = '몰리1'        
member1.username = '카다1'
member1.password = '보1'

member2.name = '몰리2'
member2.username = '카다2'
member2.password = '보2'

member3.name = '몰리3'
member3.username = '카다3'
member3.password = '보3'

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

members.append(member1_dict)                   # 과제 내용 5. 인스턴스를 빈 리스트에 append
members.append(member2_dict)
members.append(member3_dict)

# for member_dict in members:
#     print(member_dict['name'])        # 과제 내용 5-a. member 리스트를 돌면서 회원들의 이름을 모두 출력해주세요.
#     # 몰리1
#     # 몰리2
#     # 몰리3

# =========================Post 인스턴스===================================
post1 = Post()                          # 과제 내용 6. 각각의 회원이 게시글을 세 개 이상 작성하는 코드를 만들어주세요.
post2 = Post()
post3 = Post()
post4 = Post()
post5 = Post()
post6 = Post()
post7 = Post()
post8 = Post()
post9 = Post()

post1.title = "오운완1"           
post1.content = "오늘 운동 완료1"
post1.author = f"{member1.name}" 

post2.title = "오T완1"
post2.content = "오늘 TIL 완료1"
post2.author = f"{member1.name}" 

post3.title = "오S완1"
post3.content = "오늘 SQL 완료1"
post3.author = f"{member1.name}" 

post4.title = "오운완2"
post4.content = "오늘 운동 완료2"
post4.author = f"{member2.name}" 

post5.title = "오T완2"
post5.content = "오늘 TIL 완료2"
post5.author = f"{member2.name}" 

post6.title = "오S완2"
post6.content = "오늘 SQL 완료2"
post6.author = f"{member2.name}" 


post7.title = "오운완3"
post7.content = "오늘 운동 완료3"
post7.author = f"{member3.name}" 

post8.title = "오T완3"
post8.content = "오늘 TIL 완료3"
post8.author = f"{member3.name}" 

post9.title = "오S완3"
post9.content = "오늘 SQL 완료3"
post9.author = f"{member3.name}" 

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

posts.append(post1_dict)                  # 과제내용 6. 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요.
posts.append(post2_dict)
posts.append(post3_dict)
posts.append(post4_dict)
posts.append(post5_dict)
posts.append(post6_dict)
posts.append(post7_dict)
posts.append(post8_dict)
posts.append(post9_dict)

# for post in posts:                       # 과제 내용 6-a. for문을 돌면서 특정 유저가 작성한 게시글의 제목을 모두 출력해주세요.
#     if post['author'] == '몰리1':
#         print(post['title'])

# # 오운완1
# # 오T완1
# # 오S완1

# for post in posts:                        # 과제내용 6-b. for문을 돌면서 '특정 단어'가 content에 포함된 게시글의 제목을 모두 프린트 해주세요.
#     if '운동' in post['content']:
#         print(post['title'])

# # 오운완1
# # 오운완2
# # 오운완3

# ===========================추가 도전 과제 .ver=============================================
'''
print("<<회원가입을 환영합니다.>>")
print("=========================")
print("약관 : 안녕 hello")

create_instance_or_not = input("약관에 동의하십니까? (y/n): ")

if create_instance_or_not == "y": # 약관에 동의하면
    member_a = Member()         # 인스턴스 생성

member_a.name = input("이름을 적어주세요: ")          # 추가 도전 과제 1.
member_a.username = input("활동명을 적어주세요: ")    # 사용자가 터미널에서 Member 인스턴스 생성하기.
member_a.password = input("비밀번호를 적어주세요: ")  # (input을 이용한다.)

members = []

member_a_dict = {}
member_a_dict["name"] = member_a.name
member_a_dict["username"] = member_a.username
member_a_dict["password"] = member_a.password

members.append(member_a_dict)

print(members)
# [{'name': '가', 'username': '나', 'password': '다'}]

# -------------------post-----------------------------
add_post = input("게시글을 작성하시겠습니까? (y/n): ")

if add_post == 'y':
    post_a = Post()

post_a.title = input("게시글의 제목을 지어주세요: ")    # 추가 도전 과제 2.
post_a.content = input("내용을 적어주세요: ")          # post도 터미널에서 생성할 수 있게 해주세요.
post_a.author = f"{member_a.name}" 

posts = []

post_a_dict = {}
post_a_dict["title"] = post_a.title
post_a_dict["content"] = post_a.content
post_a_dict["author"] = post_a.author

posts.append(post_a_dict)

print(posts)
# [{'title': '라', 'content': '마', 'author': '가'}]
'''


# =======================================================================================================================
# **추가 도전 과제:**

# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# 2. post도 터미널에서 생성할 수 있게 해주세요.
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

# =======================================================================================================================
# **평가**

# - 클래스와 인스턴스 개념을 설명할 수 있는가?    클래스는 동일한 정보/기능을 가진 개체들을 생성하는 역할을 합니다.
#                                              인스턴스는 클래스를 통해 만드는 개체입니다.
# - 메소드와 어트리뷰트(속성)을 설명할 수 있는가? 어트리뷰트는 1차원적인 정보를 가지고, 이를 통해 각 인스턴스를 구분지을 수 있습니다.
#                                              메소드는 인스턴스가 활용할 수 있는 기능입니다.
# - 클래스를 정의할 수 있는가? 클래스는 속성과 메소드를 통해 인스턴스를 생성할 수 있습니다. 클래스에서 정의하는 함수를 메소드라고 부릅니다.
#                            클래스를 파일로 저장하여 모듈의 기능으로 동작합니다. from 모듈 import 클래스
# - 인스턴스를 생성할 수 있는가? '인스턴스이름 = 클래스이름()' 을 통하여 인스턴스를 생성할 수 있습니다.