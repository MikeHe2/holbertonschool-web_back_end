#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school document into the specified MongoDB collection.
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        **kwargs: Keyword arguments representing the fields and values of the school document.
    Returns:
        str: The inserted document's ID.
    """


    documents = mongo_collection.insert_one(kwargs)

    return documents.inserted_id
