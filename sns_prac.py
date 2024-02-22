class Member():                # ()괄호를 사용해도 실행이 되고, 괄호를 사용하지 않아도 실행이 되는데, 어떤 기능이 있나요?
    name = ""
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


member1.display()            # display()메소드 사용
member2.display()
member3.display()

members = []
# print(type(members))
# print(type(member1))   # member1의 타입은 <class '__main__.Member'>

members = members.append(member1) 
# print(members) # !!! print(members)의 출력이 None이다.

# members = members.append(member2) # AttributeError: 'NoneType' object has no attribute 'append'
# members = members.append(member3) 


# print(members)