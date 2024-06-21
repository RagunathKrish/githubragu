class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("RAM:",self.ram)
        print("Processor:",self.processor)
hp=laptop()
dell=laptop()

hp.ram="8GB"
hp.processor="i5"

dell.ram="16GB"
dell.processor="i7"

hp.display()
dell.display()
