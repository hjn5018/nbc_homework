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
