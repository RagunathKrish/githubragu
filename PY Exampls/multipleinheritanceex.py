class dad():
    def phone(self):
        print("Dad's Phone")
class mom(dad):
    def sweet(self):
        print("Mom's sweet")
class son(mom):
    def laptop(self):
        print("son's laptop")
ram=son()
ram.sweet()
deep=mom()
deep.phone()
ram.phone()
        
