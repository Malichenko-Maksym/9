class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'P({self.x},{self.y})'
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "Same points, distance=0"
        else: return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
q=Point(0,0)
w=Point(4,3)
print(q==w)