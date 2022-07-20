import pymongo

client = pymongo.MongoClient("mongodb+srv://y7me909:Vedansh2020@cluster0.cukc5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"mahesh",
    "email":"host2gmail.com",
    "empid":"9001"
}

db1 = client['mongot1']
coll = db1['t1']
coll.insert_one(d)