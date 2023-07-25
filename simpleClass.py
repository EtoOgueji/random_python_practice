class Person:
    def say_hi(self):
        print("Hello how are you")

p = Person()

p.say_hi()

class Robot:
    pass


x = Robot()
y = Robot()

x.name = "Marvin"
x.build_year = "1979"

y.name = "Caliban"
y.build_year = "1993"

print(x.name)
print(y.build_year)

print(x.__dict__)


class Robot1(object):
    Robot.brand = "OGUEJI ROCKEBOTICS"

def f(x):
    return x
f.x = 45
print(f.x)

def hi(obj):
    print("Hi, I am " + obj.name + "!")


class Robot:
    pass


x = Robot()
x.name = "Marvin"
hi(x)
