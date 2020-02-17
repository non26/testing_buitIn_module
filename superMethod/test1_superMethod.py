"""
    this super method example here takes the argument of two,
    first is the subClass and the second is the instance of that subClass
    so that the the subClass' instance can use the superClass' attributes
    STRUCTURE:
        super(subclass, instance)
"""
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

class Square(Rectangle):
    def __init__(self, length):
        # super() executes fine now
        super(Square, self).__init__(length, length)

s = Square(5)
print(s.area)  # 25