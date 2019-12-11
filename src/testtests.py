import unittest


def divide(x, y):
    if x and y:
        return (x / y)
    else:
        return -1


class TestMath(unittest.TestCase):
    def test_divide_returns_correct_result(self):
        # Arranage - setup the environment
        test_x = 20
        test_y = 10

        # Act
        result = divide(test_x, test_y)

        # Assert
        self.assertEqual(result, 2, "Should be 2")

    def test_divide_fails_when_dividing_by_zero(self):
        # Arranage - setup the environment
        test_x = 20
        test_y = 0

        # Act
        result = divide(test_x, test_y)

        # Assert
        self.assertEqual(result, -1, "Should fail")

        #self.assertRaises(ZeroDivisionError, divide, test_x, test_y)


if __name__ == "__main__":
    unittest.main()
