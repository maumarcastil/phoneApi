import pymongo
##My key mongo: cJe0TE8AQ7PFGcKU

client = pymongo.MongoClient(
    "mongodb+srv://maumarcastil:<password>@cluster0.d72qs.mongodb.net/phone_api")

print(client.list_database_names())