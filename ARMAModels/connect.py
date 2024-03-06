from ARMAModels.connect import MongoClient
# Creating my connection to MongoDB server
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi =db["nairobi"]