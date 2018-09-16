from peewee import *

db = SqliteDatabase('worklog.db')


class Entry(Model):
    name = TextField(default=0)
    task_name = TextField(default=0)
    minutes_worked = TextField(default=0)
    additional_notes = TextField(default=0)
    timestamp = TextField(default=0)

    class Meta:
        database = db

def initialize():
    """create the database and table if the don't exist"""
    db.connect('worklog.db')
    db.create_tables([Entry], safe=True)

