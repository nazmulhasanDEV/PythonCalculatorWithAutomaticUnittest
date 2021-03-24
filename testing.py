import unittest
import calculator
import csv

class TestMain(unittest.TestCase):

    def testingAddition(self):
        with open('./Unit Test Addition.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                arg2 = int(converting_into_list[x][x-x+1])
                result = int(converting_into_list[x][x-x + 2])
                main_func = calculator.Calculator().addition(arg1, arg2)
                self.assertEqual(main_func, result)


    def testingSubtraction(self):
        with open('./Unit Test Subtraction.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                arg2 = int(converting_into_list[x][x-x+1])
                result = int(converting_into_list[x][x-x + 2])
                main_func = calculator.Calculator().subtraction(arg1, arg2)
                self.assertEqual(main_func, result)

    def testingMultiplication(self):
        with open('./Unit Test Multiplication.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                arg2 = int(converting_into_list[x][x-x+1])
                result = int(converting_into_list[x][x-x + 2])
                main_func = calculator.Calculator().multiplication(arg1, arg2)
                self.assertEqual(main_func, result)

    def testingDivision(self):
        with open('./Unit Test Division.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                arg2 = int(converting_into_list[x][x-x+1])
                result = int(converting_into_list[x][x-x + 2])
                main_func = calculator.Calculator().division(arg1, arg2)
                self.assertEqual(main_func, result)

    def testingSquare(self):
        with open('./Unit Test Square.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                # arg2 = int(converting_into_list[x][x-x+1])
                result = int(converting_into_list[x][x-x + 1])
                main_func = calculator.Calculator().square(arg1)
                self.assertEqual(main_func, result)

    def testingSquareRoot(self):
        with open('./Unit Test Addition.csv', 'r') as addition:
            data = csv.reader(addition)
            converting_into_list = list(data)
            for x in range(1, len(converting_into_list)):
                arg1 = int(converting_into_list[x][x - x])
                result = int(converting_into_list[x][x-x + 1])
                main_func = calculator.Calculator().square_root(arg1)
                self.assertEqual(main_func, result)


if __name__ == '__main__':
    unittest.main()
