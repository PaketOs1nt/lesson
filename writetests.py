import logging
import unittest

from coloramaa import * # дз

logging.basicConfig(level=logging.DEBUG, format=f"[{__name__}:%(levelname)s] (%(asctime)s) - %(message)s")

logging.debug('asdasdasd')

class MyTest(unittest.TestCase):
    def test_args(self):
        self.assertEqual(asd(2, 2), 4)

if __name__ == '__main__':
    unittest.main()