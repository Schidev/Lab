import unittest


class TestListMethods(unittest.TestCase):

    def test_roman_tkalenko_fi_13(self):
        self.assertEqual(len([]), 0)
        self.assertEqual(len(['a']), 1)
        self.assertEqual(len(['a', 'b']), 2)

    def test_denis_schifrin_fi_93(self):
        self.assertEqual(5, 2)

if __name__ == '__main__':
    unittest.main()
