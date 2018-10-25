from pymongo import DESCENDING

from init_db import db


def build_index(col, field):
    col.create_index([(field, DESCENDING)])


if __name__ == '__main__':
    build_index(db.lg, 'key')
    build_index(db.lg, 'sub_key')
