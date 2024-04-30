#!/usr/bin/env python3
''' Define the schools_by_topic method '''


def schools_by_topic(mongo_collection, topic):
    ''' Returns the list of school having a specific topic '''
    result = list(mongo_collection.find({"topics": topic}))
    return result
