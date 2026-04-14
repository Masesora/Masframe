from pymongo import MongoClient
from functools import lru_cache
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("MONGO_DB_NAME", "CLINICA")

@lru_cache()
def get_database():
    client = MongoClient(MONGO_URI)
    return client[DATABASE_NAME]

def clients_collection():
    return get_database()["masesora"]["clients"]

def client_codes_collection():
    return get_database()["masesora"]["client_codes"]

def client_symptom_states_collection():
    return get_database()["masesora"]["client_symptom_states"]

def internal_users_collection():
    return get_database()["masesora"]["internal_users"]

def ese_registros_collection():
    return get_database()["masesora"]["ese_registros"]