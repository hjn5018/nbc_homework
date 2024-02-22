class Member:
    name = ""
    username = ""
    password = ""
    def display(self):
        print(self.name, self.username)

class Post:
    title = ""
    content = ""
    author = "" # !!! username이 저장되어야 함!!!

# member1 = Member("몰리") # TypeError: Member() takes no arguments
# member2 = Member("카다")
# member3 = Member("보")

member1 = Member()
member2 = Member()
member3 = Member()


member1.name = '몰리'
member1.username = '카다'
member1.password = '보'

member1.display()

members = []
# print(type(members))
# print(type(member1))   # member1의 타입은 <class '__main__.Member'>

members = members.append(member1) 
# print(members) # !!! print(members)의 출력이 None이다.

# members = members.append(member2) # AttributeError: 'NoneType' object has no attribute 'append'
# members = members.append(member3) 


# print(members)