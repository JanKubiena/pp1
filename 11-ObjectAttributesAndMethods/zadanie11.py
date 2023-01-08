import math

class figures_area():

    @staticmethod
    def rectangle(height, width):
        area = height * width
        return area

    @staticmethod
    def triangle(height, base):
        area = (height * base) / 2
        return area

    @staticmethod
    def circle(radius):
        area = math.pi * math.pow(radius, 2)
        return area


print(figures_area.rectangle(4.5,7))
print(figures_area.triangle(6,2))
print(figures_area.circle(3))