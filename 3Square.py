class Square:
    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("Size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return self.__size ** 2


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
