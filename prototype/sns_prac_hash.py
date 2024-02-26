from pprint import pprint    # 보기 좋게 출력하기
import hashlib


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

create_instance_or_not = input("약관에 동의하십니까? (y/n): ") # Member 인스턴스 생성 준비

if create_instance_or_not == "y": # 약관에 동의하면
    member_a = Member()         # 인스턴스 생성

member_a.name = input("이름을 적어주세요: ")          # 추가 도전 과제 1.
member_a.username = input("활동명을 적어주세요: ")    # 사용자가 터미널에서 Member 인스턴스 생성하기.
member_a.password = input("비밀번호를 적어주세요: ")  # (input을 이용한다.)
# =============================비밀번호 해싱==============================
iters = 100000    # 일반적인 반복 횟수
dk = hashlib.pbkdf2_hmac('sha256', b'member_a.password', b'madna', iters)
# brute-force attack을 대비한 pbkdf2_hmac
# madna라는 salt를 password에 섞어서 sha256으로 해싱한다.

members = []

member_a_dict = {}
member_a_dict["name"] = member_a.name
member_a_dict["username"] = member_a.username
member_a_dict["password"] = dk.hex()    # 비밀번호를 헥사값(16진법)으로 담는다.
# ========================================================================
members.append(member_a_dict)    # 리스트에 인스턴스 정보 추가

# print(members)    # 잘 들어갔는지 확인
# # [{'name': '가', 'username': '나', 'password': 'af9528d336182011095c5334f677f221e02d2a69208db75a4ca541dfb9504d29'}]    # 확인 완료

# -------------------post-----------------------------
add_post = input("게시글을 작성하시겠습니까? (y/n): ")    # Post 인스턴스 생성 준비

if add_post == 'y':    # 동의하면
    post_a = Post()    # 인스턴스 생성

post_a.title = input("게시글의 제목을 지어주세요: ")    # 추가 도전 과제 2.
post_a.content = input("내용을 적어주세요: ")          # post도 터미널에서 생성할 수 있게 해주세요.
post_a.author = f"{member_a.name}" 

posts = []    # post 인스턴스들의 정보를 담은 딕셔너리를 모아놓을 리스트 생성

post_a_dict = {}    # post 인스턴스의 정보를 담을 딕셔너리 생성
post_a_dict["title"] = post_a.title
post_a_dict["content"] = post_a.content
post_a_dict["author"] = post_a.author

posts.append(post_a_dict)    # 인스턴스의 딕셔너리를 리스트에 추가

# print(posts)                                          # 잘 들어갔는지 확인
# # [{'title': '라', 'content': '마', 'author': '가'}]   # 확인 완료 
