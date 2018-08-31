#!/usr/bin/env python3

from collections import OrderedDict
from prompts import AddEntry
import datetime
import os
import sys

from peewee import *

db = SqliteDatabase('diafy.db')


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
    db.connect('diary.db')
    db.create_tables([Entry], safe=True)

def clear():
    """clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """show the menu"""

    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items(): print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """add an entry"""
    print("Enter your entry. Press ctrl+d when finished")
    # Captures everything the user types until the enter an end of file key sequence.
    # You get the file key sequence by pressing clrl+d
    # data = sys.stdin.read().strip()
    moe = AddEntry()

    # if data:
        # anything other than the letter N
        # if input('Save entry? [Yn] ').lower() != 'n':

    work_log = Entry(name=moe.name(), task_name=moe.task_name(), minutes_worked=moe.time_spent(),
                     additional_notes=moe.notes())
    work_log.save()

def view_entries(column, search_query=None):
    """view previous entries"""

    if column == 'name':
        field_name = Entry.name
    elif column == 'task_name':
        field_name = Entry.task_name
    elif column == 'date':
        field_name = Entry.timestamp
    elif column == 'minutes_worked':
        field_name = Entry.minutes_worked
    else:
        field_name = Entry.additional_notes

    # print(field_name, "this is fieldname")

    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(field_name.contains(search_query))

    # print(entries, "this")

    for entry in entries:
        # timestamp = entry.timestamp.strftime('%A %B %D, %Y %I:%M%p')
        # timestamp = entry.timestamp
        # clear()
        # print(timestamp)
        # print('='*len(timestamp))
        print("Name:", entry.name)
        print("Task name:", entry.task_name)
        print("Time spent:", entry.minutes_worked, "minutes")
        print("Notes:", entry.additional_notes)
        # print("\n\n"+'='*len(timestamp))
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input('Action: [Ndq]').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)

        if next_action == "a":
            entriess = entries.where(Entry.name)
            print(entriess)

def search_prints():
    """Prints information to the screen"""
    print("a) find by employee")
    print("b) find by date")
    print("c) find by time spent")
    print("d) find by search term")

def search_entries():
    """search entries for a string"""
    search_prints()
    searchyy = input("How do you want to search?").lower().strip()

    if searchyy == 'a':
        search_name_entries()
    if searchyy == 'b':
        search_date_entries()
    if searchyy == 'c':
        search_minutes_entries()
    if searchyy == 'd':
        search_notes_entries()

def search_name_entries():
    """Prints every entry entry inside the name column"""
    print("Here are the name entries: ")
    name_list = []
    for name in Entry.select():
        name_list.append(name.name)
    for name in set(name_list):
        print(name)
    while True:
        user = input("Who do you want to see entries from? ")
        if user in set(name_list):
            view_entries('name', user)
            break
        else:
            continue
            #try again

def search_date_entries():
    print("Here are the dates of when users added an entry: ")
    date_list = []
    for date in Entry.select():
        date_list.append(date.timestamp)
    for date in date_list:
        print(date)
    while True:
        date_entered = input("Which date do you want to see entries from? ")
        if date_entered in set(date_list):
            view_entries('date', date_entered)
            break
        else:
            continue
                # try again
        #something that doesn't allow invalid date
        #so if it's not in the list then don't call the function

def search_minutes_entries():
    print("here are the time spent")
    minutes_list = []
    for time in Entry.select():
        minutes_list.append(str(time.minutes_worked))
    for time in set(minutes_list):
        print(time)
    while True:
        print(set(minutes_list))
        minutes = (input("who do you want to see entries from?"))
        if minutes in set(minutes_list):
            print(minutes)
            view_entries('minutes_worked', str(minutes))
            break
        else:
            continue

def search_notes_entries():
    notes_list = []
    for task_name in Entry.select():
        notes_list.append(task_name.task_name)
    for notes in Entry.select():
        notes_list.append(notes.additional_notes)
        print(notes_list)
    while True:
        notes_search = input("who do you want to see entries from?")
        if notes_search in notes_list:
            view_entries(notes_search)
    ##That entry is not stored try again sir!!!!

def delete_entry(entry):
    """delete an entry"""
    if input("Are you sure? [yN] ").lower() == 'y':
        entry.delete_instance()
        print("Entry deleted")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])

if __name__=='__main__':
    initialize()
    menu_loop()