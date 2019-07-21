class Vehicle:
    def general_purpose(self):
        print("I am  a vhehicle and i am used for Trnasportation ")

class Car(Vehicle):
    def __init__(self):
        print("I am a Car")
        self.wheel = 4
        self.covered = True

    def specific_use(self):
        print("Used for vacation by family")

class MotoCycle(Vehicle):
    def __init__(self):
        print("I am a Motocylcle")
        self.wheel = 2
        self.covered = False

    def specific_use(self):
        print("it is used for reoadtrips ")




c = Car()
c.specific_use()
c.general_purpose()

print('\n new line ')
m = MotoCycle()
m.specific_use()
m.general_purpose()
m.wheel

print('\nThis is a new program below')

     ### Multi Class inheritance  ###

class Father:
    def programming(self):
        print('i love programing computers')


class Mother:
    def cooking(self):
        print( 'i love cooking meals')

#Now this child class want to inhereit attributes of the two parent class

class Child(Father, Mother):
    def skills(self):
        print(' i love sports and watching movies')



c = Child()
c.skills()
c.programming()
c.cooking()


print('\nThis is a new program below   PART 2')

     ### Multi Class inheritance  part 2  ###

class Father:
    def skills(self):
        print('i love programing computers')


class Mother:
    def skills(self):
        print( 'i love cooking meals')

#Now this child class want to inhereit attributes of the two parent class

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print(' i love sports and watching movies')



c = Child()
c.skills()


