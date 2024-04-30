#!/usr/bin/env python3
''' Lists all documents in a collection '''


def list_all(mongo_collection):
    '''List all documents'''
    result = list(mongo_collection.find())
    if len(result) == 0:
        return []
    return result
