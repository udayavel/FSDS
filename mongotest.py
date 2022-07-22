import pymongo

client = pymongo.MongoClient("mongodb+srv://Udayavel:root@cluster0.gqsn3hi.mongodb.net/?retryWrites=true&w=majority")
db = client.test


print(db)

d={
    'name':'Udayavel',
    'emailid':'udayavel.g@gmail.com',
    'surname':'G'
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)