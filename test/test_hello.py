import unittest

from drumline.hello import Hello


class MyTestCase(unittest.TestCase):
    def test_hello(self):
        expected = "Hello World"
        result = Hello.hello_world()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
