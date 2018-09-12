#!/usr/bin/env python3

from unittest.mock import patch, call
import unittest

import work_log
from prompts import AddEntry

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prompts = AddEntry()
        self.entry = work_log

    # def setUp(self):
    #     add_entries.db.connect()
    #     add_entries.db.create_tables(add_entries.Entry, safe=True)
    #
    #
    # def test_check_user_table(self):
    #     assert add_entries.Entry.table_exists()
    #
    #
    # def tearDown(self):
    #     try:
    #         add_entries.db.drop_tables(add_entries.Entry)
    #     except:
    #         pass
    #     add_entries.db.close()

    def test_input_is_int(self):
        with patch('builtins.input', side_effect=[8]) as mock:
            result = self.prompts.time_spent()
            self.assertIsInstance(result, int)

    def test_input_can_be_negative_number(self):
        with patch('builtins.input', side_effect=[-2]) as mock:
            result = self.prompts.time_spent()
            self.assertIsInstance(result, int)

    def test_name_input_is_string(self):
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.name()
            self.assertIsInstance(result, str)

    def test_task_name_input_is_string(self):
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.task_name()
            self.assertIsInstance(result, str)

    def test_notes_input_is_string(self):
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = self.prompts.notes()
            self.assertIsInstance(result, str)

    def test_menu(self):
        self.assertIsInstance(work_log.menu, dict)

    def test_no(self):
        with patch('builtins.input', side_effect=["adf", 'q']) as mock:
            result = work_log.search_notes_entries()
            self.assertNotEqual(work_log.Entry.task_name, result)


    # def test_l(self):
    #     with patch('builtins.input', side_effect=["v"]) as mock:
    #         result = add_entries.menu_loop()
    #         self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
