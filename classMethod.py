# class Calculator:
#     num1 = int(input("Enter first number: "))
#
#     @staticmethod
#     def operations():
#         operation_list = ['A', '+', 'S', '-', 'M', '*', 'D', '/', '**', 'sr', 'SR', 'exit', 'Exit']
#         operation_type = input("Enter operation type(A,+=addition, S,- =subtraction, M,*=multiplication, D,/ =division, S,**=square, SR/sr=square root, exit/Exit=exit the operation): ")
#         if operation_type not in operation_list:
#             return False
#         return operation_type
#
#     def addition(self):
#         num2 = int(input("Enter second number: "))
#         total = self.num1 + num2
#         return f'Addition= {total}'
#
#     def subtraction(self):
#         num2 = int(input("Enter second number: "))
#         total = self.num1 - num2
#         return f'Subtraction= {total}'
#
#     def multiplication(self):
#         num2 = int(input("Enter second number: "))
#         total = self.num1 * num2
#         return f'Multiplication= {total}'
#
#     def division(self):
#         num2 = int(input("Enter second number: "))
#         total = self.num1 / num2
#         return f'Division= {total}'
#
#     def square(self):
#         total = self.num1 ** 2
#         return f'Square of {self.num1} is {total}'
#
#     def square_root(self):
#         total = self.num1 ** 0.5
#         return f'Square root of {self.num1} is: {total}'
#
#
#     @classmethod
#     def calculation(cls, operation_type):
#         if operation_type == 'A' or operation_type == '+':
#             return cls.addition(self=cls)
#
#         elif operation_type == 'S' or operation_type == '-':
#             return cls.subtraction(self=cls)
#
#         elif operation_type == '*' or operation_type == 'M':
#             return cls.multiplication(self=cls)
#
#         elif operation_type == '':
#             return "Must enter operation type"
#
#         elif operation_type == False:
#             return "Must enter valid operation type"
#
#         elif operation_type == '**':
#             return cls.square(self=cls)
#
#         elif operation_type == "SR" or operation_type == 'sr':
#             return cls.square_root(self=cls)
#
#         else:
#             return False
#
#
#
# while True:
#     operation_type = Calculator.operations()
#     if operation_type == 'exit' or operation_type == 'Exit':
#         break
#     print(Calculator.calculation(operation_type))
#
