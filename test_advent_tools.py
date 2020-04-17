import unittest
import advent_tools

class TestBrackets(unittest.TestCase):
    def test_inside_outside_simple(self):
        test_str = 'ab(cd)e(f)ghi'
        exp_outside = ['ab', 'e', 'ghi']
        exp_inside = ['cd', 'f']
        inside, outside = advent_tools.get_inside_outside_brackets(test_str,
                                                                   '(', ')')
        self.assertEqual(exp_inside, inside)
        self.assertEqual(exp_outside, outside)

    def test_recursive_simple(self):
        test_str = 'ab(cd)e(f)ghi'
        exp_outside = ['ab', 'e', 'ghi']
        exp_inside = ['cd', 'f']
        expected_result = {'inside': exp_inside, 'outside': exp_outside}
        result = advent_tools.recursive_inside_outside(test_str, '(', ')')
        self.assertEqual(expected_result, result)

    def test_inside_outside_nested(self):
        test_str = 'ab(cd(jk))e(f)ghi'
        exp_outside = ['ab', 'e', 'ghi']
        exp_inside = ['cd(jk)', 'f']
        inside, outside = advent_tools.get_inside_outside_brackets(test_str,
                                                                   '(', ')')
        self.assertEqual(exp_inside, inside)
        self.assertEqual(exp_outside, outside)

    def test_recursive_nested(self):
        test_str = 'ab(cd(jk))e(f)ghi'
        expected_result = {'outside': ['ab', 'e', 'ghi'],
                           'inside': [{'outside': ['cd'],
                                       'inside': ['jk']}, 'f']}
        result = advent_tools.recursive_inside_outside(test_str, '(', ')')
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
