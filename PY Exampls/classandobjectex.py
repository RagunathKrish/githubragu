class goa:
    name=""
    drink=""
    def party(self):
        print("let's Party!!!!")
    def beach(self):
        print("Enjoy the Beach .......")

ramesh = goa()
suresh = goa()

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink="Yes"
suresh.drink="No"

print(ramesh.name)
print("Drink:",ramesh.drink)
ramesh.party()
print(suresh.name)
print("Drink:",suresh.drink)
suresh.beach()
