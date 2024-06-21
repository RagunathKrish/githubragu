class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def funct(self):
        print("add:",self.num1+self.num2)
        print("sub:",self.num1-self.num2)
        print("Mul:",self.num1*self.num2)
        print("Div:",self.num1/self.num2)

obj1=calculator(10,2)
obj1.funct()
