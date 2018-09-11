from unittest.mock import patch, call
import unittest

import add_entries
from prompts import AddEntry

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prompts = AddEntry()


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


    def test_search_by_term(self):
        """Checks to see if search_by_term calls the correct method"""

        # Create a user_input variable to hold onto the input statement
        # we will fake into input()

        user_input = ['hello', 'ignored_second_value']
        # The second string never gets called and is ignored in this method

        # We can patch the input() statements by over-riding 'builtins.input'
        # side_effect can take the list of items we want to put into
        # the input call
        with patch('builtins.input', side_effect=user_input):

            # Here we are patching the view_entries method so it does not
            # get called.
            # Notice we need the full path to it with 'classes.'
            with patch('classes.add.view_entries') as view_entry_patch:
                # Now we need to call the function so everything will run
                # and the mock object will get triggered
                self.work_log.search_by_term()

        # The patch view_entry_patch will hold onto whether or not it was
        # called and with what variables.

        view_entry_patch.assert_called_with(["Notes"], "\\bhello\\b", "", "")

        # Everything checks out




    def test_input_can_be_negative_number(self):
        entry = AddEntry()
        with patch('builtins.input', side_effect=[-2]) as mock:
            result = entry.time_spent()
            self.assertIsInstance(result, int)

    def test_name_input_is_string(self):
        entry = AddEntry()
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = entry.name()
            self.assertIsInstance(result, str)

    def test_task_name_input_is_string(self):
        entry = AddEntry()
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = entry.task_name()
            self.assertIsInstance(result, str)

    def test_notes_input_is_string(self):
        entry = AddEntry()
        with patch('builtins.input', side_effect=["string"]) as mock:
            result = entry.notes()
            self.assertIsInstance(result, str)

    def test_menu(self):
        self.assertIsInstance(add_entries.menu, dict)

    # def test_l(self):
    #     with patch('builtins.input', side_effect=["v"]) as mock:
    #         result = add_entries.menu_loop()
    #         self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
