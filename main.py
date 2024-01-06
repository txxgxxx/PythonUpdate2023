
class GuardDog:

    def __init__(self, name, breed):
        self.name = name
        self.age = 5
        self.breed = breed

    def grr(self):
        print("stay away!")

class Puppy:

    def __init__(self, name, breed):
        self.name = name
        self.age = 0.1
        self.breed = breed

    def __str__(self):
        return f"{self.breed} named {self.name}"
    
    def woof_woof(self):
        print("Woof Woof!")

    def introduce(self):
        self.woof_woof()
        print(f"my name is {self.name} and i am a baby {self.breed}")
        self.woof_woof()

ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = Puppy(name="Bibi", breed="Dalmatian")

ruffus.introduce()
bibi.introduce()