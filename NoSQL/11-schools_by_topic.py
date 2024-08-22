#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools from the given MongoDB collection that match the specified topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to search in.
        topic (str): The topic to filter the schools by.

    Returns:
        pymongo.cursor.Cursor: A cursor object containing the matching school documents.
    """

    documents = mongo_collection.find({"topics": topic})

    return documents
