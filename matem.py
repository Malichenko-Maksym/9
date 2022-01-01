class matem():
    @staticmethod
    def triangle_area(base,heigh):
        return 0.5*base*heigh
    def rectangle_area(first_side,second_side):
        return first_side*second_side
    def circle_area(radius):
        import math
        return math.pi*radius**2
print(matem.circle_area(3))
print(matem.rectangle_area(4,7))
print(matem.triangle_area(6,2))