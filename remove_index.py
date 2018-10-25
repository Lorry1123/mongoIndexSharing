import json
from init_db import db


def get_all_indexes(col):
    info = col.index_information()
    info.pop('_id_')
    return info.keys()


def remove_all_indexes(col):
    index_names = get_all_indexes(col)
    for name in index_names:
        col.drop_index(name)


if __name__ == '__main__':
    print 'before remove, indexes:\n'
    print json.dumps(db.lg.index_information(), indent=4)
    remove_all_indexes(db.lg)
    print 'after remove:\n', get_all_indexes(db.lg)
