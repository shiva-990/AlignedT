class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print("config is: ", self.cpu,self.ram)

com1=computer()
com2=computer('i7',8)
com1.config('i5',16)
com2.config()



