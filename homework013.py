class Furniture:

    def __init__(self, my_height, my_width, my_length):
        self.my_height = my_height
        self.my_width = my_width
        self.my_length = my_length
        self.my_square = float(my_width * my_length)
        self.my_volume = float(my_width * my_length * my_height)


class Bed(Furniture):
    def __int__(self, my_height, my_width, my_length):
        super().__init__(my_height, my_width, my_length)


class Table(Furniture):
    def __int__(self, my_height, my_width, my_length):
        super().__init__(my_height, my_width, my_length)

def __add__(self, other, other2):
    return float(self.my_volume + other.my_volume)


table_1 = Table(80, 250, 100)
bed_1 = Bed(70, 380, 260)
print(table_1.my_volume, bed_1.my_volume)
print(float.__add__(table_1.my_volume, bed_1.my_volume))