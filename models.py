import math

class Calculator:
    def __init__(self):
        self.name = "Calculator ProMax LuxeDeluxe"

   def add(self, num1, num2):
        return round(num1 + num2,ndigits=5)

    def subtract(self, num1, num2):
        return round(num1 - num2,ndigits=5)

    def multiply(self, num1, num2):
        return round(num1 * num2,ndigits=5)

    def divide(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is undefined."
        return round(num1 / num2,ndigits=5)

    def power(self, num1, num2):
        return round(num1 ** num2,ndigits=5)

    def square_root(self, num):
        if num < 0:
            return "Error: Cannot take the square root of a negative number."
        return round(math.sqrt(num),ndigits=5)
