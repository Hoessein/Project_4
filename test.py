import unittest

import add_entries
from prompts import AddEntry

class MyTestCase(unittest.TestCase):
    def test_time_input(self):
        add_entryy = AddEntry()
        pr = add_entryy.time_spent()
        assert isinstance(pr, int)

        # self.assertEqual(True, False)

    def test_twt(self):
        assert not 1 + 1 == 3


if __name__ == '__main__':
    unittest.main()
