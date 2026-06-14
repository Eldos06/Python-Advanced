import unittest

def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть от 0 до 100%")
    return price * (1 - discount / 100)

# https://docs.python.org/3/library/unittest.html

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()

















