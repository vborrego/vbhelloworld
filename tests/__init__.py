import unittest
from vbhelloworld import add
from vbhelloworld import main
from os.path import expanduser
from os.path import isfile
from os import remove

class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdd(self):
        self.assertEqual(5,  add(3,2) )
        
    def testMain(self):
        conffile=expanduser('~/testhelloworld.conf')
        main(conf_file = conffile )
        self.assertEqual(True, isfile(conffile) )
        remove(conffile)
        self.assertEqual(False, isfile(conffile) )
        
if __name__ == '__main__':
    unittest.main()

