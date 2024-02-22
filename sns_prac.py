class Member():                # ()괄호를 사용해도 실행이 되고, 괄호를 사용하지 않아도 실행이 되는데, 어떤 기능이 있나요?
    name = ""                  # *arg 써봐도 괜찮을 듯?
    username = ""
    password = ""
    def display(self):
        print(self.name, self.username)

class Post():
    title = ""
    content = ""
    author = "" # !!! username이 저장되어야 함!!!

# member1 = Member("몰리") # TypeError: Member() takes no arguments
# member2 = Member("카다")
# member3 = Member("보")

member1 = Member()            # 인스턴스 생성
member2 = Member()
member3 = Member()

member1.name = '몰리1'        # 인스턴스 속성 부여
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


members.append(member1.name)
members.append(member2.name)
members.append(member3.name)


# members = members.append(member2) # AttributeError: 'NoneType' object has no attribute 'append'
# members = members.append(member3) 


# members.append("1") # append test
# print(members)      # append test

for member in members:
    print(member)        # 과제 5-a


# 1. member1이 게시글을 세 개 이상 작성하는 코드를 만들자.        //과제 6의 일부
# (post의 인스턴스 3개 생성)
    
# 풀이 :
# author는 회원의 username이 저장되어야한다.
# author를 member1으로 하고, title, content를 속성으로 하는 post클래스의 instance를 생성하자. 

post1 = Post()
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
posts_title = []

posts_title.append(post1.title)
posts_title.append(post2.title)
posts_title.append(post3.title)
posts_title.append(post4.title)
posts_title.append(post5.title)
posts_title.append(post6.title)
posts_title.append(post7.title)
posts_title.append(post8.title)
posts_title.append(post9.title)

# print(posts_title)
# # ['오운완1', '오T완1', '오S완1']

posts_content = []

# for i in [1, 2, 3]: # for문 쉽지 않네...
#     posts_content.append(post(i).content) # NameError: name 'post' is not defined
#     # print(i)

posts_content.append(post1.content)
posts_content.append(post2.content)
posts_content.append(post3.content)
posts_content.append(post4.content)
posts_content.append(post5.content)
posts_content.append(post6.content)
posts_content.append(post7.content)
posts_content.append(post8.content)
posts_content.append(post9.content)

# print(posts_content)
# # ['오늘 운동 완료1', '오늘 TIL 완료1', '오늘 SQL 완료1']

posts_author = []

posts_author.append(post1.author)
posts_author.append(post2.author)
posts_author.append(post3.author)
posts_author.append(post4.author)
posts_author.append(post5.author)
posts_author.append(post6.author)
posts_author.append(post7.author)
posts_author.append(post8.author)
posts_author.append(post9.author)

# print(posts_author)
# # ['몰리1', '몰리1', '몰리1']

# print(posts_title, posts_content, posts_author) # 확인 완료

