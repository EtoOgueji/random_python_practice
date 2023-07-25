# getters and setters
# they are used to protect objects from assigning bad field values to them or to provide improved output

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property  # used to refer to individual fields in the __init__ function
    # defining individual field functions
    def height(self):
        print("Retrieving the height")

        return self.__height  # __ to protect our data.

    @height.setter # to prevent us from inserting bad data into the field
    def height(self, value):

        if value.isdigit():  # to make sure it's a digit
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property  # refer to individual fields
    # defining field function
    def width(self):
        print("Retrieving the width")

        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for height")

    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    eSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    eSquare.height = height
    eSquare.width = width

    print("Height: ", eSquare.height)
    print("Width: ", eSquare.width)

    print("The Area is: ", eSquare.getArea())