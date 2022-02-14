import unittest
from hoge import MyClass, MyClass2

class TestMyClass2(unittest.TestCase):
    """test class of MyClass2"""

    def setUp(self):
        print(f"setUp")

    def tearDown(self):
        print(f"tearDown")

    def test_get_text(self):
        mc = MyClass2("hoge", 123)
        actual = mc.get_text()
        expected = "123-hoge"
        self.assertEqual(expected, actual)

    @unittest.skip("not implemented")
    def test_add(self):
        mc = MyClass()
        expected = 3
        self.assertEqual(expected, mc.add((1, 2, "hoge")))

if __name__ == "__main__":
    unittest.main()

