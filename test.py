from unittest.mock import patch
import unittest

import work_log
from prompts import AddEntry

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prompts = AddEntry()
        self.entry = work_log

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

    def test_if_notes_or_taskname_input_is_in_database(self):
        with patch('builtins.input', side_effect=["python testing", 'q']) as mock:
            result = work_log.search_notes_entries()
            self.assertEqual(work_log.Entry.task_name, result)

    def test_if_minutes_is_in_database(self):
        with patch('builtins.input', side_effect=["40000", 'q']) as mock:
            result = work_log.search_minutes_entries()
            self.assertEqual(work_log.Entry.minutes_worked, result)

    def test_if_date_entry_is_in_database(self):
        with patch('builtins.input', side_effect=["hoessein", 'q']) as mock:
            result = work_log.search_name_entries()
            self.assertNotEqual(work_log.Entry.task_name, result)

if __name__ == '__main__':
    unittest.main()
