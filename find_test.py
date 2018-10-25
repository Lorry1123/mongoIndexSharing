from time import time
from random import randint

from init_db import db


def find_test(col, times):
    st = time()
    while times:
        target = randint(1, 100)
        tmp = col.find_one({'sub_key': target})
        times -= 1
    ed = time()
    return ed - st


if __name__ == '__main__':
    test_times = 10
    lg_time = find_test(db.lg, test_times)
    print 'db.lg costs ', lg_time, 's'
    sm_time = find_test(db.sm, test_times)
    print 'db.sm costs ', sm_time, 's'
