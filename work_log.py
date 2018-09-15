#!/usr/bin/env python3

from collections import OrderedDict
from prompts import AddEntry
import os

from database import Entry, initialize

def clear():
    """clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """show the menu"""

    choice = None

    while choice != 'q':
        clear()
        print("Welcome, in this appliciation you can store your work activities!\n")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('\nAction: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_entry():
    """add an entry"""
    add = AddEntry()

    work_log = Entry(name=add.name(), task_name=add.task_name(), minutes_worked=add.time_spent(),
                     additional_notes=add.notes())
    print("Thank you, Your entry was saved succesfully\n")
    work_log.save()


def view_entries(column=None, search_query=None):
    """view previous entries"""

    entries = Entry.select().order_by(Entry.timestamp.desc())

    if column == 'name':
        field_name = Entry.name
        name_query = entries.where(field_name.contains(search_query))
        printer(name_query)
    elif column == 'task_name':
        field_name = Entry.task_name
        task_query = entries.where(field_name.contains(search_query))
        printer(task_query)
    elif column == 'date':
        field_name = Entry.timestamp
        date_query = entries.where(field_name.contains(search_query))
        printer(date_query)
    elif column == 'minutes_worked':
        field_name = Entry.minutes_worked
        minutes_query = entries.where(field_name.contains(search_query))
        printer(minutes_query)
    else:
        notes_task_search = Entry.select().where(Entry.task_name.contains(search_query) |
                                                 Entry.additional_notes.contains(search_query))
        printer(notes_task_search)

def printer(entries):
    """prints entries for each row in the database"""
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %D, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print("Name:", entry.name)
        print("Task name:", entry.task_name)
        print("Time spent:", entry.minutes_worked, "minutes")
        print("Notes:", entry.additional_notes)
        print('='*len(timestamp)+"\n")
        print('n) next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input('\nAction: [Ndq]').lower().strip()
        if next_action == 'q':
            menu_loop()
            break
        elif next_action == 'd':
            delete_entry(entry)

        #
        # if next_action == "a":
        #     entriess = entries.where(Entry.name)
        #     print(entriess)

def search_prints():
    """Prints information to the screen"""
    print("a) find by employee")
    print("b) find by date")
    print("c) find by time spent")
    print("d) find by search term")

def search_entries():
    """search entries"""
    search_prints()
    # if the database is empty the user won't be allowed to search for an entry.
    if Entry.select().where(Entry.name.is_null(False)):

        while True:
            search = input("\nHow do you want to search? ").lower().strip()
            if search == 'a':
                clear()
                search_name_entries()
            if search == 'b':
                clear()
                search_date_entries()
            if search == 'c':
                clear()
                search_minutes_entries()
            if search == 'd':
                clear()
                search_notes_entries()
            else:
                clear()
                search_prints()
    else:
        print("The database is empty, first add an entry before you can search. ")

def search_name_entries():
    """Prints every entry entry inside the name column"""
    print("Here are all the name entries: \n")
    name_list = []
    for name in Entry.select():
        name_list.append(name.name)
    for name in set(name_list):
        print(name)
    while True:
        user = input("\nWho do you want to see entries from? ")
        for x in set(name_list):
            if user in x:
                view_entries('name', user)
                menu_loop()
                return
        else:
            clear()
            print("That name is not available, try again!\n")
            search_name_entries()
            continue

def search_date_entries():
    print("Here are the dates of when users added an entry:\n ")
    date_list = []
    set_date_list = []
    counter = 1
    for date in Entry.select():
        date_list.append(date.timestamp)
    for date in set(date_list):
        set_date_list.append(date)
        print(counter,":", date)
        counter += 1
    while True:
        try:
            date_entered = int(input("\nWhich date do you want to see entries from? "))
            if date_entered >= 1:
                date_entered -= 1
                view_entries('date', set_date_list[date_entered])
                menu_loop()
                return
        except (IndexError, ValueError):
            clear()
            print("Not a valid entry, please enter an available number!\n")
            search_date_entries()
            continue

def search_minutes_entries():
    print("Here are the amount of minutes users worked on an entry: \n")
    minutes_list = []
    for time in Entry.select():
        minutes_list.append(str(time.minutes_worked))
    for time in set(minutes_list):
        print(time)
    while True:
        minutes = (input("\nWhich amount do you want to see entries from? "))
        if minutes in set(minutes_list):
            view_entries('minutes_worked', str(minutes))
            menu_loop()
            return
        else:
            clear()
            print("Not a valid entry try again.\n")
            search_minutes_entries()
            continue

def search_notes_entries():
    notes_list = []
    task_name_list = []
    for task_name in Entry.select():
        task_name_list.append(task_name.task_name)
    for notes in Entry.select():
        notes_list.append(notes.additional_notes)
    while True:
        print (notes_list, "this is the notes")
        print (task_name_list, "this is taskname")
        notes_search = input("Which search entry would you like to make? ")
        print(notes_search, "this test")
        for x in notes_list:
            if notes_search in x:
                view_entries(' ', notes_search)
                menu_loop()
                return
        # elif notes_search in task_name_list:
        #     # view_entries('task_name', notes_search)
        else:
            clear()
            print("Not a valid entry try again\n")
            search_notes_entries()
            continue

def delete_entry(entry):
    """delete an entry"""
    if input("Are you sure? [yN] ").lower() == 'y':
        entry.delete_instance()
        print("Entry deleted")

menu = OrderedDict([
    ('a', add_entry),
    ('s', search_entries)
])

if __name__=='__main__':
    initialize()
    menu_loop()

##afsluiten van menutjes
##na het tonen van de resultaten
##alles moet netjes worden afgesloten