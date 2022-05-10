class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return int(self.width) * int(self.height)

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pic = ""
        picture = ""
        i = 0
        j = 0
        if self.width > 50:
            return "Too big for picture."
        else:
            while i < int(self.width):
                pic += "*"
                i += 1
            while j < int(self.height):
                picture += pic + "\n"
                j += 1
            return picture

    def get_amount_inside(self, shape):
        x = 0
        y = 0
        if self.height > shape.height:
            y = self.height // shape.height
        if self.width > shape.width:
            x = self.width // shape.width
        return x * y


class Square(Rectangle):
    def __init__(self, side, width=0, height=0):
        super().__init__(width, height)
        self.side = side
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side
        self.side = side
