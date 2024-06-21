class student:
    def __init__(self):
        self.name="name"
        self.regno="543"
    def display(self):
        print("Name",self.name)
        print("Regno",self.regno)
s1=student()
s2=student()

s1.name="Ramesh"
s1.regno="789"

s2.name="Suresh"
s2.regno="678"

s1.display()
s2.display()
