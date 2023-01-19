class person:

    #__init__ is Instance Methods
    # self refers to the object we created in the class

    def __init__(self, name, age, colorskin, country):
        self.name = name
        self.age = age
        self.country = country
        self.colorskin = colorskin

    def person(self):
       print(self.name + ": " +str(age) +str(colorskin) +str(country))

        