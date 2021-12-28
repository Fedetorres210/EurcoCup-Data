from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
connection = MongoClient(f"mongodb+srv://{user}:{password}@cluster0.rdiud.mongodb.net/test")
