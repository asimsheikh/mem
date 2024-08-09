from datetime import datetime 

from typing import NamedTuple

import fastlite as fl

class Log(NamedTuple): id: int; text: str; created: datetime


def test_db_create():
    db = fl.database(':memory:')

    db.t.log.create(Log.__annotations__, pk='id')
    logs = [Log(id=None, text='Adding the first entry', created=datetime.now()),
            Log(id=None, text='See if we can finalise development', created=datetime.now())]
    db.t.log.insert_all(map(lambda x: x._asdict(), logs))
    result = db.q(f'select * from {db.t.log}')
    assert len(result) == 2

    db.t.log.drop()

