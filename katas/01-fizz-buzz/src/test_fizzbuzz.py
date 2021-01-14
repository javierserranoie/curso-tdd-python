import unittest

def list_to_100():
    list_100 = []
    for i in range(1,101):
        list_100.append(modify_multiple_of_3_or_5(i))
    return list_100

def modify_multiple_of_3_or_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

class FizzBuzzTest(unittest.TestCase):
    def test_something(self):
        result = list_to_100()
        self.assertEqual(len(result), 100)

    def test_multiple_of_3(self):
        result = list_to_100()
        self.assertEqual(result[2], "Fizz")
        self.assertEqual(result[95], "Fizz")

    def test_multiple_of_5(self):
        result = list_to_100()
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[99], "Buzz")

    def test_multiple_of_3_and_5(self):
        result = list_to_100()
        self.assertEqual(result[14], "FizzBuzz")
        self.assertEqual(result[59], "FizzBuzz")