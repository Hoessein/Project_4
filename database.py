from collections import OrderedDict
from prompts import AddEntry
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('worklog.db')


class Entry(Model):
    name = TextField(default=0)
    task_name = TextField(default=0)
    minutes_worked = TextField(default=0)
    additional_notes = TextField(default=0)
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """create the database and table if the don't exist"""
    db.connect('worklog.db')
    db.create_tables([Entry], safe=True)

# entries = Entry.select().order_by(Entry.timestamp.desc())
#
# # entries = entries.where(
# #     Entry.additional_notes.contains("python") & entries.where(Entry.task_name.contains("python")))
# #
# # for x in entries:
# #     print(x.task_name, x.additional_notes)
#
# variable = "python"
#
# # print([entry.task_name for entry in entries])
# # var = Entry.select().where(Entry.task_name.contains(variable) | Entry.additional_notes.contains(variable))
#
# var = entries.where(Entry.task_name.contains(variable) | (Entry.additional_notes.contains(variable)))
#
#
# for x in var:
#     print(x.name, x.task_name, x.additional_notes)
