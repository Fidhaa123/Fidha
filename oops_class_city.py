class City:
    def addCityDetails(self,name,country):
        self.name = name
        
        
        self.country = country
    def printCityDetails(self):
        print("City Name:"+self.name)
        print("Country:"+self.country)
delhi = City()
delhi.addCityDetails("delhi","India")
delhi.printCityDetails()