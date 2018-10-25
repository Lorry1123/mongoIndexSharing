import json
from init_db import db

if __name__ == '__main__':
    query_list = list(db.system.profile.find())
    for query in query_list:
        query.pop('ts')

    print json.dumps(query_list, indent=4)
