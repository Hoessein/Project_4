# write tests

something = "poeple"

print(isinstance(something, str))


# def test_check_user_table(self):
#     assert add_entries.Entry.table_exists()


# def test_new(self):
#     self.assertIsInstance()
#
#     def search_entries():
#         """search entries for a string"""
#         search_prints()
#         # if the database is empty the user won't be allowed to search for an entry.
#         if Entry.select().where(Entry.name.is_null(False)):
#             searchyy = input("\nHow do you want to search? ").lower().strip()
#
#             if searchyy == 'a':
#                 search_name_entries()
#             if searchyy == 'b':
#                 search_date_entries()
#             if searchyy == 'c':
#                 search_minutes_entries()
#             if searchyy == 'd':
#                 search_notes_entries()
#         else:
#             print("The database is empty, first add an entry before you can search. ")


# def test_something(self):
#     self.assertTrue(add_entries.Entry.select().where(add_entries.Entry.name.is_null(False)))
#     with patch('builtins.input', side_effect=["a"]) as mock:
#         result = add_entries.search_entries()
#         self.assertIsInstance(result, str)

# def test_something(self):

# @patch('builtins.print')
# def test_print(self):
#     print('foo')
#     print()
#
#     assert add_entries.search_prints() == [call('foo'), call()]

# def test_input_is_string(self):
#     entry = AddEntry()
#     with patch('builtins.input', side_effect=["string"]) as mock:
#         result = entry.name()
#         self.assertIsInstance(result, str)

# def search_entries():
#     """search entries for a string"""
#     search_prints()
#     # if the database is empty the user won't be allowed to search for an entry.
#     if Entry.select().where(Entry.name.is_null(False)):
#         searchyy = input("\nHow do you want to search? ").lower().strip()
#
#         if searchyy == 'a':
#             search_name_entries()
#         if searchyy == 'b':
#             search_date_entries()
#         if searchyy == 'c':
#             search_minutes_entries()
#         if searchyy == 'd':
#             search_notes_entries()
#     else:
#         print("The database is empty, first add an entry before you can search. ")


# def setUp(self):
#     try:
#         add_entries.db.create_table(add_entries.Entry)
#     except:
#         pass
#     add_entries.Entry.create(
#             name='What is your name',
#             task_name='What is the taskname',
#             minutes_worked='88',
#             additional_notes="don't have additional notes")
#     add_entries.db.close()
#
# def test_create_username(self):
#     user = add_entries.Entry.get(name='testUsername')
#     self.assertEqual(user.name, 'testUsername')
#
# def test_create_task_name(self):
#     name = add_entries.Entry.get(task_name='What is the taskname')
#     self.assertEqual(name.task_name,'What is the taskname')
#
# def test_create_minutes_worked(self):
#     name = add_entries.Entry.get(minutes_worked='88')
#     self.assertEqual(name.minutes_worked,'88')
#
# def test_create_additional_notes(self):
#     name = add_entries.Entry.get(additional_notes="don't have additional notes")
#     self.assertEqual(name.additional_notes,"don't have additional notes")