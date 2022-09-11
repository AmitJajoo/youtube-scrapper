import pymongo
class Mongo:

    def insertDataMongoDb(li):
        client = pymongo.MongoClient(
            "mongodb+srv://amitkumarjajoo:<password>@cluster0.jt959jq.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        database = client['youtube']
        collection = database['details']
        collection.insert_many(li)
