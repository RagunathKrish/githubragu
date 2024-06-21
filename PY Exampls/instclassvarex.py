class laptop():
    chrger="C Type"
    def __init__ (self):
        self.brand=""
        self.price=25000

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
        
    @classmethod  
    def changechrger(cls):
        cls.chrger="B Type"
        print("Chrger type changed to B")

    @staticmethod
    def info():
        print("This is laptop class")
        
hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechrger()
hp.info()

