import unittest
from roots import find_roots


class TestFindRoots(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertEqual(find_roots(1, -3, 2), (2.0, 1.0))
        self.assertEqual(find_roots(1, 2, 1), (-1.0, -1.0))
        self.assertEqual(find_roots(
            1, 1, 2), ((-0.5+1.3228756555322954j), (-0.5-1.3228756555322954j)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, find_roots, "a", 2, 1)

    def test_special_cases_1(self):
        with self.assertRaises(ValueError) as context:
            find_roots(0, 0, 0)
        self.assertEqual(str(context.exception),
                         "Уравнение имеет бесконечно много корней.")
        
    def test_special_cases_2(self):
        with self.assertRaises(ValueError) as context:
            find_roots(0, 0, 1)
        self.assertEqual(str(context.exception),
                         "Уравнение не имеет корней.")    


if __name__ == '__main__':
    unittest.main(verbosity=2)