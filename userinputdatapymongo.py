import pymongo
from pymongo import MongoClient
import simplejson as json

client=MongoClient()
db=client.test_database
user=db.user
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
s=input("Total number of users")
s1=int(s)
list=[]
d2=user.delete_many({})
oldfile=open("./data.json","w+")
for i in range(0,s1):
    list.append("username ")
    list.append(input("Enter username "))
    list.append("password ")
    list.append(input("Enter password "))
    list.append("email ")
    list.append(input("Enter email "))
    list.append("date of birth ")
    list.append(input("Enter date of birth "))
    data=Convert(list)
    oldfile.seek(0)
    oldfile.write(json.dumps(data))
    oldfile = open("./data.json", "r+")
    data = json.loads(oldfile.read())
    user_id = user.insert_one(data).inserted_id
    db.user.create_index('userid')

result=user.find({})
for results in result:
    print(results)
c=user.find().count()
print(c)