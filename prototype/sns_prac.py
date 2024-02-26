from pprint import pprint

class Member():                # ()괄호를 사용해도 실행이 되고, 괄호를 사용하지 않아도 실행이 되는데, 어떤 기능이 있나요?
    name = ""                  # *arg 써봐도 괜찮을 듯?
    username = ""
    password = ""
    def display(self):
        print(self.name, self.username)

class Post():                  # 과제 내용 1. Member 클래스와 Post 클래스 정의
    title = ""                 # 과제 내용 2, 3, 4
    content = ""
    author = "" # !!! username이 저장되어야 함!!!

# member1 = Member("몰리") # TypeError: Member() takes no arguments
# member2 = Member("카다")
# member3 = Member("보")

member1 = Member()            # Member instance 생성 (과제 내용 5)
member2 = Member()
member3 = Member()

member1.name = '몰리1'        # Member instance에 속성 부여
member1.username = '카다1'
member1.password = '보1'

member2.name = '몰리2'
member2.username = '카다2'
member2.password = '보2'

member3.name = '몰리3'
member3.username = '카다3'
member3.password = '보3'


# member1.display()            # display()메소드 사용
# member2.display()
# member3.display()

members = []
# print(type(members))
# print(type(member1))   # member1의 타입은 <class '__main__.Member'>

# members = members.append(member1.name) # (member1.name으로 직접 빈 리스트에 append 할 수 없는 듯 하다.)가 아니고 append 사용 방법이 잘못된 듯 하다.-> 딩동댕
# print(members) # !!! print(members)의 출력이 None이다.


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

# print(member1_dict)
# print(member2_dict)
# print(member3_dict)
# {'name': '몰리1', 'username': '카다1', 'password': '보1'}
# {'name': '몰리2', 'username': '카다2', 'password': '보2'}
# {'name': '몰리3', 'username': '카다3', 'password': '보3'}


members.append(member1_dict)
members.append(member2_dict)
members.append(member3_dict)

# pprint(members)
# # [{'name': '몰리1', 'password': '보1', 'username': '카다1'},
# #  {'name': '몰리2', 'password': '보2', 'username': '카다2'},
# #  {'name': '몰리3', 'password': '보3', 'username': '카다3'}]


# members = members.append(member2) # AttributeError: 'NoneType' object has no attribute 'append'
# members = members.append(member3) 


# members.append("1") # append test
# print(members)      # append test

for member_dict in members:
    print(member_dict['name'])        # 과제 5-a
#     # 몰리1
#     # 몰리2
#     # 몰리3


# print(members[0]['name'])
# 몰리 1

# a_dict = {'가': '나'}
# print(a_dict['가'])
# # 나


# 1. member1이 게시글을 세 개 이상 작성하는 코드를 만들자.        //과제 6의 일부
# (post의 인스턴스 3개 생성)
    
# 풀이 :
# author는 회원의 username이 저장되어야한다.
# author를 member1으로 하고, title, content를 속성으로 하는 post클래스의 instance를 생성하자. 

post1 = Post() # Post instance 생성
post2 = Post()
post3 = Post()
post4 = Post()
post5 = Post()
post6 = Post()
post7 = Post()
post8 = Post()
post9 = Post()

post1.title = "오운완1"           # Post instance에 속성 부여
post1.content = "오늘 운동 완료1"
post1.author = f"{member1.name}" # ... 설마했는데.. 되네?

post2.title = "오T완1"
post2.content = "오늘 TIL 완료1"
post2.author = f"{member1.name}" 

post3.title = "오S완1"
post3.content = "오늘 SQL 완료1"
post3.author = f"{member1.name}" 

# print(post1.author) # post1.author가 정말 나오는지 확인
# print(post2.author)
# print(post3.author)


post4.title = "오운완2"
post4.content = "오늘 운동 완료2"
post4.author = f"{member2.name}" # ... 설마했는데.. 되네?

post5.title = "오T완2"
post5.content = "오늘 TIL 완료2"
post5.author = f"{member2.name}" 

post6.title = "오S완2"
post6.content = "오늘 SQL 완료2"
post6.author = f"{member2.name}" 

# print(post4.author)
# print(post5.author)
# print(post6.author)

post7.title = "오운완3"
post7.content = "오늘 운동 완료3"
post7.author = f"{member3.name}" # ... 설마했는데.. 되네?

post8.title = "오T완3"
post8.content = "오늘 TIL 완료3"
post8.author = f"{member3.name}" 

post9.title = "오S완3"
post9.content = "오늘 SQL 완료3"
post9.author = f"{member3.name}" 

# print(post7.author)
# print(post8.author)
# print(post9.author)


# 2. 만든 post 인스턴스들은 posts 빈리스트에 append써서 저장하자. //과제 6의 일부

posts = []

post1_dict = {}
post1_dict["title"] = post1.title
post1_dict["content"] = post1.content
post1_dict["author"] = post1.author

# print(post1_dict) # 확인완료
# {'title': '오운완1', 'content': '오늘 운동 완료1', 'author': '몰리1'}

post2_dict = {}
post2_dict["title"] = post2.title
post2_dict["content"] = post2.content
post2_dict["author"] = post2.author

# print(post2_dict)
# {'title': '오T완1', 'content': '오늘 TIL 완료1', 'author': '몰리1'}

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

# pprint(posts)
# [{'author': '몰리1', 'content': '오늘 운동 완료1', 'title': '오운완1'},
#  {'author': '몰리1', 'content': '오늘 TIL 완료1', 'title': '오T완1'},
#  {'author': '몰리1', 'content': '오늘 SQL 완료1', 'title': '오S완1'},
#  {'author': '몰리2', 'content': '오늘 운동 완료2', 'title': '오운완2'},
#  {'author': '몰리2', 'content': '오늘 TIL 완료2', 'title': '오T완2'},
#  {'author': '몰리2', 'content': '오늘 SQL 완료2', 'title': '오S완2'},
#  {'author': '몰리3', 'content': '오늘 운동 완료3', 'title': '오운완3'},
#  {'author': '몰리3', 'content': '오늘 TIL 완료3', 'title': '오T완3'},
#  {'author': '몰리3', 'content': '오늘 SQL 완료3', 'title': '오S완3'}]



for post in posts:                       # 과제내용 6-a
    if post['author'] == '몰리1':        # 특정유저 검색
        print(post['title'])             # 유저의 post title 출력

# 오운완1
# 오T완1
# 오S완1


for post in posts:                        # 과제내용 6-b
    if '운동' in post['content']:     # content에 특정 단어가 들어간 post 확인
        print(post['title'])            # 해당 포스트의 제목 출력

# 오운완1
# 오운완2
# 오운완3
        

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     posts[i]_dict["title"] = post[i].title
# 이렇게 할 순 없을까..

# post_list = []
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     # print(f"post{i}")
#     post_list.append(f"post{i}")

# print(post_list)
# # ['post1', 'post2', 'post3', 'post4', 'post5', 'post6', 'post7', 'post8', 'post9']

# for post in post_list:
#     print(f"{post}_dict["title"] = {post}.title") # ㅠㅠ


# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i)


# posts_title = []

# posts_title.append(post1.title)
# posts_title.append(post2.title)
# posts_title.append(post3.title)
# posts_title.append(post4.title)
# posts_title.append(post5.title)
# posts_title.append(post6.title)
# posts_title.append(post7.title)
# posts_title.append(post8.title)
# posts_title.append(post9.title)

# # print(posts_title)
# # # ['오운완1', '오T완1', '오S완1', '오운완2', '오T완2', '오S완2', '오운완3', '오T완3', '오S완3']

# posts_content = []

# # for i in [1, 2, 3]: # for문 쉽지 않네...
# #     posts_content.append(post(i).content) # NameError: name 'post' is not defined
# #     # print(i)

# posts_content.append(post1.content)
# posts_content.append(post2.content)
# posts_content.append(post3.content)
# posts_content.append(post4.content)
# posts_content.append(post5.content)
# posts_content.append(post6.content)
# posts_content.append(post7.content)
# posts_content.append(post8.content)
# posts_content.append(post9.content)

# # print(posts_content)
# # # ['오늘 운동 완료1', '오늘 TIL 완료1', '오늘 SQL 완료1', '오늘 운동 완료2', '오늘 TIL 완료2', '오늘 SQL 완료2', '오늘 운동 완료3', '오늘 TIL 완료3', '오늘 SQL 완료3']

# posts_author = []

# posts_author.append(post1.author)
# posts_author.append(post2.author)
# posts_author.append(post3.author)
# posts_author.append(post4.author)
# posts_author.append(post5.author)
# posts_author.append(post6.author)
# posts_author.append(post7.author)
# posts_author.append(post8.author)
# posts_author.append(post9.author)

# print(posts_author)
# # ['몰리1', '몰리1', '몰리1', '몰리2', '몰리2', '몰리2', '몰리3', '몰리3', '몰리3']

# print(posts_title, posts_content, posts_author) # 확인 완료

# for author in posts_author:                 # 과제 내용 6-a 연습
#     # print(username) # test
#     if author == '몰리1':
#         print(posts_title)

# ===========================================================================================================
# 풀이과정 및 회고

# 클래스, 인스턴스, 메소드는 그렇다 치는데,
# 어트리뷰트의 개념부터가 이해하기 힘들었다.
# '내가 강의로 배운 내용은 hp=100이고 alive=True인 괴물밖에 없었는데
# name, username, password는 subclass로 해야하나??
# 근데 Member 클래스의 속성이어야한다고 했는데..ㅁㄴㅇㄻㄴㄹ'

# 그러다가 method의 self 매개변수 활용법에 대해 조금 더 이해했다.
# self 매개변수는 class의 def 에서 self.hp등으로 class의 속성(attribute)와 조합하여 사용할 수 있다.
# (함수는 클래스 내부에서 정의할 때 메소드로 개념이 달리 이루어진다.)
# 또한 적어도 내가 배운 예시에서는 속성이 메소드의 매개변수로 자리잡는 일은 없었다.
# 메소드의 매개변수는 임의의 단어로 설정할 수 있고, 이는 메소드의 컨셉에 따라서 마음대로 정하면 되는 것 같다.

# 그렇게 name, username, password를 class 내부에 기술했다.
# 그리고 인스턴스를 빈 리스트에 저장하는 후반부 과정에서 착안하여
# 속성들을 빈 스트링("")으로 우선 정의했다.

# 나머지는 비교적 수월했다.
# 우선 인스턴스를 생성했다.(멤1,멤2,멤3)
# 그리고 빈 스트링으로 만들어 놓은 속성들에 내 맘대로 끄적였다.
# 사실 self.name처럼 속성을 이용하는 것은 class 안에서 def를 정의할 때 밖에 해보지 않았다.

# 경험해본 것이라고는 클래스를 공부할 때 혼자서 따라 적어보았던 monste1.damage(10)같은
# .damage()나 .check_status()같은 메소드였다.
# 그런데, 일단은 self가 인스턴스를 대표하는 posisional argument라고 생각이 들었고,
# .name으로 각 인스턴스의 내용을 채우지 않으면 뭘로 채우나? 싶어서 해봤다.

# 몇몇의 착안점은 있었지만 시도해보고 member1.display()로 속성이 잘 기입이 되었나 확인했다. ^^
# 사실 member1 = Member("몰리") 같은 시도도 해봤다.(물론 TypeError가 나왔음.)

# 이후로는 append를 사용하는 데 잘못된 사용법으로 오류가 나기도 했다.
# 잘못된 사용법 (members = members.append(member2) # AttributeError: 'NoneType' object has no attribute 'append')
# 정확한 사용법 (members.append(member1_dict))
# 여기서 append가 메소드라는 것을 인식했다. --> 맞나??

# 그리고 회원 인스턴스/ post 인스턴스를 빈 리스트에 append해서 저장하라는 말만 보고
# --------------------------------
# posts_title = []

# posts_title.append(post1.title)
# posts_title.append(post2.title)

# posts_content = []
# posts_content.append(post1.content)
# posts_content.append(post2.content)
# ...
# --------------------------------
# 같이 그냥 냅다 리스트에 박아버리기도 했다.