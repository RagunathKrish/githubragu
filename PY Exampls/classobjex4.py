class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("name",self.name)
        print("regno",self.regno)

t1=teacher("Thomas","1")
t2=teacher("John","2")

t1.display()
t2.display()

        
