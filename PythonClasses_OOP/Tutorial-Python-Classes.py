class Human:

    def __init__(self, n , g, o):
        self.name = n
        self.gender = g
        self.occupation = o

    def kind(self):
        if self.gender == "Female":
            print(self.name, "is a female")
        elif self.gender == "Male":
            print(self.name, "Is a Male")

    def do_work(self):
        if self.occupation == "Tennis Player":
            print(self.name, "Plays tennis")
        elif self.occupation == "actor":
            print(self.name, "Shoots film")

    def speaks(self):
        print(self.name, "Says how are you and is asking if you are enjoying your holliday")

    def fight(self):
        print(self.name, "Likes to fight for human rights")



    

tom = Human('Tom', "Male", "actor")
jane = Human('Jane', "Female", "Tennis Player")

tom.kind()
tom.do_work()
tom.speaks()
print('\n =====')
jane.kind()
jane.do_work()
jane.speaks()
jane.fight()
