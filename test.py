import unittest

from utils import read, count_match


class TestApp(unittest.TestCase):

    def test_reader(self):
        self.assertIsInstance(read('bug.txt'), list, 'Must be list')
        self.assertIsInstance(read('landscape.txt'), list, 'Must be list')
        self.assertIsInstance(read('landscape2.txt'), list, 'Must be list')

    def test_count_match(self):
        bug = ['| |', '###O', '| |']
        matches_1 = [(4, '| |'), (4, '###O'), (4, '| |'), (4, '| |'), (4, '###O'), (4, '| |')]
        self.assertEqual(count_match(bug, matches_1), 2, "Must be 2")
        matches_2 = [(4, '###O'), (4, '###O'), (4, '| |'), (4, '| |')]
        self.assertEqual(count_match(bug, matches_2), 0, "Must be 0")


if __name__ == '__main__':
    unittest.main()
