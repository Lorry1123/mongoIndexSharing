from init_db import db
import json

if __name__ == '__main__':
    e1 = db.lg.find({'field0': 123}).explain()
    print json.dumps(e1, indent=4), '\n\n'
    e2 = db.lg.find({'key': 123}).explain()
    print json.dumps(e1, indent=4), '\n\n'
    # explain

    e3 = db.lg.find({'sub_key': 123123}).hint('key_-1').explain()
    print json.dumps(e3, indent=4), '\n\n'
    # hint
