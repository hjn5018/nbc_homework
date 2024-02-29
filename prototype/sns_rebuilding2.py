from pprint import pprint
import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(self.name, self.username)


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


member1 = Member("몰리1", "카다1", "보1")
member2 = Member("몰리2", "카다2", "보2")
member3 = Member("몰리3", "카다3", "보3")
members = [member1, member2, member3]


post1 = Post("오운완1", "오늘 운동 완료1", member1.name)
post2 = Post("오T완1", "오늘 TIL 완료1", member1.name)
post3 = Post("오S완1", "오늘 SQL 완료1", member1.name)
post4 = Post("오운완2", "오늘 운동 완료1", member2.name)
post5 = Post("오T완2", "오늘 TIL 완료1", member2.name)
post6 = Post("오S완2", "오늘 SQL 완료1", member2.name)
post7 = Post("오운완3", "오늘 운동 완료1", member3.name)
post8 = Post("오T완3", "오늘 TIL 완료1", member3.name)
post9 = Post("오S완3", "오늘 SQL 완료1", member3.name)
posts = [post1, post2, post3, post4, post5, post6, post7, post8, post9]

member1.display()

for post in posts:
    if post.author == "몰리1":
        print(post.title)

for post in posts:
    if "운동" in post.content:
        print(post.title)

print("<<회원가입을 환영합니다.>>")
print("=========================")
print("약관 : 안녕 hello")
create_instance_or_not = input(
    "약관에 동의하십니까? (y/n): "
)  # Member 인스턴스 생성 준비
if create_instance_or_not == "y":  # 약관에 동의하면
    member_a = Member(
        input("이름을 적어주세요: "),
        input("활동명을 적어주세요: "),
        input("비밀번호를 적어주세요: "),
    )  # 인스턴스 생성
# =============================비밀번호 해싱==============================
iters = 100000  # 일반적인 반복 횟수
dk = hashlib.pbkdf2_hmac("sha256", b"member_a.password", b"madna", iters)
# brute-force attack을 대비한 pbkdf2_hmac
# madna라는 salt를 password에 섞어서 sha256으로 해싱한다.

member_a.password = dk.hex()  # 비밀번호를 헥사값(16진법)으로 담는다.
# ===========================비밀번호 해싱 끝===============================
members.append(member_a)

print(member_a.name)
print(member_a.username)
print(member_a.password) # 해싱 제대로 됐는지 확인.

add_post = input("게시글을 작성하시겠습니까? (y/n): ")  # Post 인스턴스 생성 준비
if add_post == "y":  # 동의하면
    post_a = Post(
        input("게시글의 제목을 지어주세요: "),
        input("내용을 적어주세요: "),
        member_a.name,
    )
posts.append(post_a)  # 인스턴스의 딕셔너리를 리스트에 추가

print(post_a.title)
print(post_a.content)
print(post_a.author)