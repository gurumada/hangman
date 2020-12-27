class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * self.length


class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4


a_rec = Rectangle(4, 5)

a_seq = Square(6)

print(a_rec.calculate_perimeter())
print(a_seq.calculate_perimeter())
