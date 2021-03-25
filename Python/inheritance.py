
###############################################################################
# 1. ObjectInterface: common interface for genereated objects
# 2. FactoryObject: returns object
#
# Flow:
#           client ---> [Factory ---> Abstract] <--- [Object1, Object2, ...]
#               ^                         |
#               |                         |
#               ---------------------------
#
#
###############################################################################
# Example: Animal Farm Factory

## Object Code
# 1. ObjectInterface
class Animal:
    def voice(self):
        pass

class Pig(Animal):
    def voice(self):
        print('Oink')

class Cow(Animal):
    def voice(self):
        print('Moo')
        
class Duck(Animal):
    def voice(self):
        print('Quack')

class Goat(Animal):
    def voice(self):
        print('Maaaa')

## Factory Code
# 2. FactoryObject
class AnimalFarmFactory:
    
    @staticmethod
    def getAnimal(name):
        if name == 'Duck':
            return Duck()
        elif name == 'Cow':
            return Cow()
        elif name == 'Pig':
            return Pig()
        elif name =="Goat":
            return Goat()
        else:
            assert 0, 'Could not find animal "%s"' %name

## Client Code

if __name__ == '__main__':
    
    whlie True:
    anim=input("Enter the name of the animal")
    # Create animal "Pig"
    
    if(anim=="Quit"):
         exit
    f = AnimalFarmFactory()
    animal = f.getAnimal(anim)
    animal.voice()
    ####