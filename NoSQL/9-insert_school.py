#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):

    documents = mongo_collection.insert_one(kwargs)

    return documents.inserted_id