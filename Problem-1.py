# Problem-1.py
class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            return self.a / self.b if self.b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"

# Example usage
calc = Calculator(10, 5, "add")
print("Result:", calc.calculate())
