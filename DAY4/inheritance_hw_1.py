'''
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от прямоугольника
Класс Point(x: int, y: int)

# прямоугольник создаем на основе двух точек
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property)


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали
    
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diag())
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Pint({self.x},{self.y})'

    def __repr__(self):
        return f'Pint({self.x},{self.y})'

class Rect:
    def __init__(self, po1: Point, po2: Point):
        self.p1 = po1
        self.p2 = po2


    def __str__(self):
        return f'Rect = {(abs(self.p1.x - self.p2.x))},{(abs(self.p1.y - self.p2.y))}'

    @property
    def perimetr(self):
        return 2 * (abs(self.p1.x - self.p1.x) + (self.p2.y - self.p2.y))

    @property
    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

class Square(Rect):
    def __init__(self, p1: Point, size: int):
        Rect.__init__(self, p1, Point(p1.x + size, p1.y + size))
        self.size = size

    def diag(self):
        return ((self.size ** 2) * 2) **0.5

point1 = Point(1, 1)
point2 = Point(2, 3)
point3 = Point(4, 5)
print(f'{point1 =}')
print(f'{point2 =}')
rect = Rect(point1, point2)
print(f'rect', rect)
print(f'rect area', rect.area)
print(f'rect perimetr', rect.perimetr)
sq = Square(point3, 5)
print(f' {sq =}')
print(f'square area square.area')
print(f'square perimetr', sq.perimetr)
print(f'square diag', sq.diag())
