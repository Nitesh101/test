class Shape(object):

    def __init__(self, n):
        self.number_of_sides = n
    
    def print_num_sides(self):
        print('There are ' + str(self.number_of_sides) + 'sides.')

class Square(Shape):

    def __init__(self, lengths_of_sides):
        Shape.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  
    
    def get_area(self):
        a, b, c = self.lengths_of_sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

class Rectangle(Shape):

    def __init__(self, lenghts_of_sides):
        Shape.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  
    
    def get_area(self):
        x, y = self.lenghts_of_sides
        return x * y
p = Shape(9)
p.print_num_sides()
