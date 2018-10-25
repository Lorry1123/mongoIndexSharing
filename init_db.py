from pymongo import MongoClient, SLOW_ONLY
import random

client = MongoClient('127.0.0.1', 27017)
db = client.test_db
db.set_profiling_level(SLOW_ONLY)


def data_maker(len):
    ret = []
    for _ in xrange(len):
        key1 = random.randint(1, 100)
        for _ in xrange(10):
            key2 = random.randint(1, 100)
            data = {
               'key': key1,
               'sub_key': key1 * 100 + key2,
               'field_0': str(key1) + str(key2) + str(random.randint(1, 100)),
               'field_1': key1 * key2 + random.randint(1, 100),
            }
            ret.append(data)
    return ret


def init_sm_collection():
    sm_collection = db.sm
    data = data_maker(100)
    sm_collection.insert_many(data)


def init_lg_collection():
    lg_collection = db.lg
    data = data_maker(100000)
    lg_collection.insert_many(data)


if __name__ == '__main__':
    init_sm_collection()
    init_lg_collection()
