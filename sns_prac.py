class Member:
    name = ""
    username = ""
    password = ""
    def display(self, name, username):
        print(self.name, self.username)

class Post:
    title = ""
    content = ""
    author = "" # !!! username이 저장되어야 함!!!

# member1 = Member("몰리") # TypeError: Member() takes no arguments
# member2 = Member("카다")
# member3 = Member("보")

Moly = Member()
Kada = Member()
Bo = Member()

members = []

members = members.append(Moly) # AttributeError: 'NoneType' object has no attribute 'append'
members = members.append(Kada)
members = members.append(Bo)

print(member)