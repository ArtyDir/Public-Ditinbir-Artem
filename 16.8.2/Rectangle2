from Rectangle import Rectangle, Square, Circle

Rect1 = Rectangle(5,10)
Rect2 = Rectangle(10,20)

print("Area1=", Rect1.get_area())
print("Area2=", Rect2.get_area())

Square1 = Square(5)
Square2 = Square(10)

print("Square1=", Square1.get_area_square())
print("Square2=", Square2.get_area_square())

Circle1 = Circle(5)
Circle2 = Circle(10)

print("Circle1=", Circle1.get_area_circle())
print("Circle2=", Circle2.get_area_circle())

figures = [Rect1, Rect2, Square1, Square2, Circle1, Circle2]
for figure in figures:
    if isinstance(figure, Square):
        print("Square area=", figure.get_area_square())
    else:
        print("Area of a rectangle=", figure.get_area())
else:
    print("Area of a circle=", figure.get_area_circle())
