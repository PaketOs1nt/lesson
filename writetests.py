import logging
import unittest

from coloramaa import * # дз

logging.basicConfig(level=logging.DEBUG, format=f"[{__name__}:%(levelname)s] (%(asctime)s) - %(message)s")




@capturetime
def test_capture():
    time.sleep(3)
    return 1+3



class TestCapturing(unittest.TestCase):
    def test_custom(self):
        self.assertEqual(test_capture(), (4, 3.0)) # 4: регультат, 3.0: ожидаемое время выполнения
    
    def test_normal(self):
        self.assertEqual(capturetime(time.sleep)(9.1), (None, 9.1))

if __name__ == '__main__':
    unittest.main()