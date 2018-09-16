from unittest.mock import patch
import unittest
import io
import sys

import work_log
from prompts import AddEntry
from database import Entry


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prompts = AddEntry()
        self.entry = work_log

    def test_input_is_int(self):
        """tests if the input of minutes is an int"""
        with patch('builtins.input', side_effect=[8]) as mock:
            result = self.prompts.time_spent()
            self.assertIsInstance(result, int)

    def test_input_can_be_negative_number(self):
        """tests if the input of minutes can be a negative number"""
        with patch('builtins.input', side_effect=[-2]) as mock:
            result = self.prompts.time_spent()
            self.assertIsInstance(result, int)

    def test_name_input_is_string(self):
        """tests if the name of the employee is a str"""
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.employee()
            self.assertIsInstance(result, str)

    def test_task_name_input_is_string(self):
        """tests if task name is a str"""
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.task_name()
            self.assertIsInstance(result, str)

    def test_date_is_datetime(self):
        """tests if datetime.strftime input is a str"""
        with patch('builtins.input', side_effect=["12/05/2018"]) as mock:
            result = self.prompts.task_date()
            self.assertIsInstance(result, str)

    def test_notes_input_is_string(self):
        """tests if notes input is a str"""
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.notes()
            self.assertIsInstance(result, str)

    def test_menu(self):
        """tests if work log menu is a dict"""
        self.assertIsInstance(work_log.menu, dict)

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.prompts = AddEntry()
        self.entry = work_log
        self.date = '11/07/2011'
        self.employee = 'hoessein'
        self.task_name = 'learning to write unittests'
        self.minutes = '800'
        self.notes = 'i really love liverpool'
        self.cap = io.StringIO()
        sys.stdout = self.cap

    def test_entries_created(self):
        """tests if entries can be made to the database"""
        with patch('builtins.input', side_effect=[self.date, self.employee, self.task_name, self.minutes, self.notes]) as mock:
            self.entry.add_entry()
            #asserts if the colum Entry.name is not empty
            assert Entry.select().where(Entry.name.is_null(False))

    def test_employee_created(self):
        """tests if the created employee entry matches the input"""
        assert Entry.name == self.employee

    def test_task_name_created(self):
        """tests if the created task name entry matches the input"""
        assert Entry.task_name == self.task_name

    def test_minutes_created(self):
        """tests if the created minutes entry matches the input"""
        assert Entry.minutes_worked == self.minutes

    def test_notes_created(self):
        """tests if the created notes entry matches the input"""
        assert Entry.additional_notes == self.notes

    def test_dates_created(self):
        """tests if the created date entry matches the input"""
        assert Entry.timestamp == self.date

    def test_if_search_methods_prints_are_made(self):
        """tests if prints are made to the console"""
        self.entry.search_prints()
        print('Captured', self.cap.getvalue())

    def test_if_entries_prints_are_made(self):
        """tests if prints are made to the console"""
        self.entry.printer("")
        print('Captured', self.cap.getvalue())

    def test_if_employee_can_be_search_and_program_is_exited(self):
        """tests if entree is in database and finally the program can be exited"""
        with self.assertRaises(SystemExit):
            with patch('builtins.input', side_effect=[self.employee, "e"]) as mock:
                self.entry.search_name_entries()

    def test_if_date_can_be_searched_and_program_is_exited(self):
        """tests if entree is in database and finally the program can be exited"""
        with self.assertRaises(SystemExit):
            with patch('builtins.input', side_effect=[self.date, "e"]) as mock:
                self.entry.search_date_entries()

    def test_if_minute_can_be_searched_and_program_is_exited(self):
        """tests if entree is in database and finally the program can be exited"""
        with self.assertRaises(SystemExit):
            with patch('builtins.input', side_effect=[self.minutes, "e"]) as mock:
                self.entry.search_minutes_entries()

    def test_if_task_name_can_be_searched_and_program_is_exited(self):
        """tests if entree is in database and finally the program can be exited"""
        with self.assertRaises(SystemExit):
            with patch('builtins.input', side_effect=[self.task_name, "e"]) as mock:
                self.entry.search_note_and_task_name_entries()

    def test_if_notes_can_be_searched_and_program_is_exited(self):
        """tests if entree is in database and finally the program can be exited"""
        with self.assertRaises(SystemExit):
            with patch('builtins.input', side_effect=[self.notes, "e"]) as mock:
                self.entry.search_note_and_task_name_entries()

if __name__ == '__main__':
    unittest.main()
