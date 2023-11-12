import unittest
from math_quiz import function_random_value, function_operator, function_calculate


class TestMathGame(unittest.TestCase):

    def test_function_random_value(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_random_value(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_operator(self):
        # Test for valid operators returned
        valid_operators = ['+', '-', '*', '/']
        generated_operator = function_operator()
        self.assertIn(generated_operator, valid_operators)

    def test_function_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 7, '*', '4 * 7', 28),
            (10, 2, '/', '10 / 2', 5),

            
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, ans = function_calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(ans, expected_answer)

if __name__ == "__main__":
    unittest.main()
