from pprint import pprint

class Member():                
    name = ""                  
    username = ""
    password = ""
    def display(self):
        print(self.name, self.username)

class Post():                  
    title = ""                 
    content = ""
    author = "" 

member1 = Member()            
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

members.append(member1_dict)
members.append(member2_dict)
members.append(member3_dict)

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

posts.append(post1_dict)
posts.append(post2_dict)
posts.append(post3_dict)
posts.append(post4_dict)
posts.append(post5_dict)
posts.append(post6_dict)
posts.append(post7_dict)
posts.append(post8_dict)
posts.append(post9_dict)
