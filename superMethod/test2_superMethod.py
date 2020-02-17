"""
    This is legal in the Python 3.x
    ,without super method's argument, it's illegal in the Python 2.x
"""
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

class Square(Rectangle):
    def __init__(self, length):
        # no arguments provided to super()
        super().__init__(length, length)

s = Square(8)
print(s.area)  # does not execute
