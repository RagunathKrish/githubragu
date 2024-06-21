class phone():
    def __init__(self,brand,price,chrger):
        self.brand=brand
        self.price=price
        self.chrger=chrger

    def display(self):
        print("brand",self.brand)
        print("price",self.price)
        print("charger",self.chrger)

samsung=phone("samsung","10000","B-Type")
samsung.display()

vivo=phone("VivoV25","25000","C-Type")
vivo.display()

        
