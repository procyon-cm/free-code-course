class Rectangle:
    width = 0
    height = 0


    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = int(self.width) * int(self.height)
        return area
    
    def get_perimeter(self):
        perimeter =  2 * int(self.width) + 2 * int(self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = (int(self.width ** 2 + int(self.height) ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if int(self.width) > 50 or int(self.height) > 50:
            return "Too big for picture."
        else:
            lst = list()
            line = '*' * int(self.width)
            for i in range(int(self.height)):
                lst.append(line)
            picture = '\n'.join(lst)
            picture = picture + "\n"
            return picture
   
    def get_amount_inside(self, self.Rectangle):
        if self.height < Rectangle.height or self.width < Rectangle.width:
            return 0
        else:
            num_width = self.width // Rectangle.width
            num_height = self.height // Rectangle.height
            result = int(num_height) * int(num_width)
            return result

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side
    
    def set_height(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"
