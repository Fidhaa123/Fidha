class Person():
    cityName = "Mumbai"
    def printName(self,name):
        print(name)
class AAA(Person):
    def printDetails(self):
        print("Babitha the power girl")
class BBBBBBB(Person):
    def printDetails(self):
        print("Babitha the power girl")        
obj = AAA()
obj.cityName = "new city"
obj.printName("AAA")
obj = BBBBBBB()
obj.cityName = "new city"
obj.printName("BBBBBBB")