from shapes import (
    Shape,
    Circle,
    Rectangle,
    ShapeMeta,
)


def show_shape_details(shape: Shape) -> None:
    print("Got shape", shape)
    print("Its area is", shape.area)
    print("And perimeter is", shape.perimeter)


def show_all_shapes() -> None:
    for name, cls in ShapeMeta.shapes.items():
        print("Shape", repr(name), "is", cls)

    print()
    for name, cls in Circle.shapes.items():
        print("Shape", repr(name), "is", cls)


def main():
    show_all_shapes()
    print()

    circle_a = Circle(2)
    circle_b = Circle(3)
    rectangle_a = Rectangle(5, 7)
    rectangle_b = Rectangle(7, 7)

    for shape in (
        circle_a,
        circle_b,
        rectangle_a,
        rectangle_b,
    ):
        print("+")
        show_shape_details(shape)

    print()
    print("also circle_a's circumference is", circle_a.circumference)
    print("also circle_b's circumference is", circle_b.circumference)

    try:
        circle_b.radius = 0
    except ValueError as e:
        print("could not update circle_b.radius, got error:", e)
    try:
        rectangle_a.width = -1
    except ValueError as e:
        print("could not update rectangle_a.width, got error:", e)


if __name__ == "__main__":
    main()