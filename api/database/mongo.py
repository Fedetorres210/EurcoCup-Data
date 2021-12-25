from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

user = os.getenv(USERNAME)
password= os.getenv(PASSWORD)
url = f""
connection = MongoClient(url)

db = connection.get_database('')