import unittest
from vbhelloworld import add

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdd(self):
        self.assertEqual(5,  add(3,2) )

if __name__ == '__main__':
    unittest.main()

