class Member():
    def name(self, name):
        self.name

    def username(self, username):
        self.username

    def password(self, password):
        self.password

    def display(self, name, username):
        print(self.name, self.username)


class Post():
    def title(self, title):
        self.title
    
    def content(self, content):
        self.content

member1 = Member("몰리") # TypeError: Member() takes no arguments
member2 = Member("카다")
member3 = Member("보")

members = []

members = members.append(member1)
members = members.append(member2)
members = members.append(member3)

print(member)