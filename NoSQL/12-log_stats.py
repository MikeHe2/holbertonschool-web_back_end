#!/usr/bin/env python3
"""This is a task"""

from pymongo import MongoClient


def log_status():
    """
    Retrieves and prints statistics about the nginx logs.

    Retrieves the total number of logs and prints it.
    Retrieves the count of each HTTP method used in the logs and prints them.
    Retrieves the count of status check logs and prints it.
    """

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx

    total_logs = nginx_logs.count_documents({})

    print(f"{total_logs} logs")
    print("Methods:")

    for method in methods:

        counter = nginx_logs.count_documents({"method": method})
        print(f"\tmethod {method}: {counter}")

    status_check = nginx_logs.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print(f"{status_check} status check")


if __name__ == "__main__":
    log_status()
