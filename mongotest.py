import pymongo


client = pymongo.MongoClient("mongodb+srv://Udayavel:root@cluster0.gqsn3hi.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    'name':'udaya',
    'email':'test@gmail.com',
    'surname':'vel'
}

db1=client['mongotest']
col=db1['test']
col.insert_one(d)