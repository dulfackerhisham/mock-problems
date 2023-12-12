class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
n1 = int(input("enter 1st number "))
n2 = int(input("enter 2nd number "))

obj1 = Calculator(n1, n2)

result1 = obj1.add()
result2 = obj1.subtract()
print(f"{n1} + {n2} = {result1}")
print(f"{n1} - {n2} = {result2}")
