class phone():
    chrger="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        

    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("charger",self.chrger)
phone.chrger="B-type"
samsung=phone("samsung","10000")
samsung.display()

vivo=phone("VivoV25","25000")
vivo.display()
