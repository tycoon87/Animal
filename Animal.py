class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    def walk(self):
        self.health -= 1
        return self
        
    def run(self):
        self.health -= 5
        return self
        
    def display(self):
        print "{} health is {}".format(self.name, self.health)
    
character1 = Animal("bare",100)
character1.run().walk().display() 
    
class dog(Animal):
    def __init__(self,name):
        super(dog, self).__init__(name,150)

    def pet(self):
        self.health += 5
        return self
        
character2 = dog("woofie")
character2.run()
        
class dragon(Animal):
    def __init__(self,name):
        super(dragon,self).__init__(name,170)
        
    def fly(self):
        self.health += 10
        return self
        
    def Ddisplay(self,display):
        super(dragon, self).display()
        print "iam a dragon"
        return self

character3 = dragon("fire")
character3.fly().run().walk().display()