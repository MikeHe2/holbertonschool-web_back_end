#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Retrieve all documents from a MongoDB collection.
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to retrieve documents from.
    Returns:
        pymongo.cursor.Cursor: A cursor object containing all the documents from the collection.
    """

    documents = mongo_collection.find()

    return documents