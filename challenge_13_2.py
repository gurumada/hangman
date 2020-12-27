class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size


squ = Square(100)
print(squ.s1)
print(squ.calculate_perimeter())
squ.change_size(500)
print(squ.s1)
