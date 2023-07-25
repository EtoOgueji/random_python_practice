# Real World Objects: Attributes and Capabilities
# self allows an object to refer to itself

class Dog:

    # defining attributes (or fields)
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    # defining capabilities
    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("Spot", 66, 26)

    spot.bark()

    bowser = Dog()

    bowser.bark()

main()