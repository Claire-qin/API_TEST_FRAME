import unittest

class TestDemo(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(1+1,2)

if __name__ == '__main__':
    unittest.main()