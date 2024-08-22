#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Update the topics field of documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update.
        name (str): The name of the documents to update.
        topics (list): The new list of topics to set.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.

    """

    documents = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return documents