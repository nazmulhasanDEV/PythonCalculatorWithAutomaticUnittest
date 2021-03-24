class Calculator:
    # num1 = int(input("Enter first number: "))

    @staticmethod
    def operations():
        operation_list = ['A', '+', 'S', '-', 'M', '*', 'D', '/', '**', 'sr', 'SR', 'exit', 'Exit']
        operation_type = input("Enter operation type(A,+=addition, S,- =subtraction, M,*=multiplication, D,/ =division, S,**=square, SR/sr=square root, exit/Exit=exit the operation): ")
        if operation_type not in operation_list:
            return False
        return operation_type

    @staticmethod
    def addition(num1, num2):
        total = num1 + num2
        return total

    @staticmethod
    def subtraction(num1, num2):
        total = num1 - num2
        return total

    @staticmethod
    def multiplication(num1, num2):
        total = num1 * num2
        return total

    @staticmethod
    def division(num1, num2):
        total = num1 / num2
        return total

    @staticmethod
    def square(num1):
        total = num1 ** 2
        return total

    @staticmethod
    def square_root(num1):
        total = num1 ** 0.5
        return total


    @classmethod
    def calculation(cls, operation_type):

        if operation_type == 'A' or operation_type == '+':

            num2 = int(input("Enter second number: "))

            return cls.addition(cls.num1, num2)

        elif operation_type == 'S' or operation_type == '-':
            num2 = int(input("Enter second number: "))
            return cls.subtraction(cls.num1, num2)

        elif operation_type == '*' or operation_type == 'M':
            num2 = int(input("Enter second number: "))
            return cls.multiplication(cls.num1, num2)

        elif operation_type == '':
            return "Must enter operation type"

        elif operation_type == False:
            return "Must enter valid operation type"

        elif operation_type == '**':
            return cls.square(cls.num1)

        elif operation_type == "SR" or operation_type == 'sr':
            return cls.square_root(cls.num1)

        else:
            return False




# operation_type = Calculator.operations()
# print(Calculator.calculation(operation_type))

