class Calculator:
    def __init__(self,operation,num1,num2):
        self.operation = operation
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2


res =   Calculator("suma",5,7)
print("suma: ",res.suma())