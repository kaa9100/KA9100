import pytest
from polygon import Polygon


class TestPolygon:

    def test_polygon_initialization(self):
        polygon = Polygon("Triangle", [3, 3, 3])
        assert polygon.get_name() == "Triangle", f"Expected 'Triangle', got {polygon.get_name()}"
        assert polygon.get_sides() == [3, 3, 3], f"Expected [3, 3, 3], got {polygon.get_sides()}"

    def test_get_name(self):
        """ Verifying that the (Name) Accessor is executing properly, with the correct output """
        polygon = Polygon("Square", [4, 4, 4, 4])
        assert polygon.get_name() == "Square", f"Expected 'Square', got {polygon.get_name()}"

    def test_set_name(self):
        """ Verifying that the (Name) Mutator is executing properly, with the correct output """
        polygon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])
        polygon.set_name("Pentagon")
        assert polygon.get_name() == "Pentagon", f"Expected 'Pentagon', got {polygon.get_name()}"

    def test_get_sides(self):
        """ Verifying that the (Sides) Accessor is executing properly, with the correct output """
        polygon = Polygon("Triangle", [3, 3, 3])
        assert polygon.get_sides() == [3, 3, 3], f"Expected [3, 3, 3], got {polygon.get_sides()}"

    def test_set_sides(self):
        """ Verifying that the (Sides) Mutator is executing properly, with the correct output """
        polygon = Polygon("Square", [4, 4, 4, 4])
        polygon.set_sides([5, 5, 5, 5])
        assert polygon.get_sides() == [5, 5, 5, 5], f"Expected [5, 5, 5, 5], got {polygon.get_sides()}"

    def test_polygon_inequality(self):
        """ Let's verify that our special method __ne__, inequalize when providing the same object with different values """
        polygon1 = Polygon("Triangle", [3, 3, 3])
        polygon2 = Polygon("Square", [4, 4, 4, 4])
        assert polygon1 != polygon2, "Expected polygon1 != polygon2"

    def test_polygon_equality(self):
        """ Let's verify that our special method __eq__, equalize when providing the same object with same values """
        polygon1 = Polygon("Triangle", [3, 3, 3])
        polygon2 = Polygon("Triangle", [3, 3, 3])
        assert polygon1 == polygon2, "Expected polygon1 == polygon2"

    def test_polygon_str(self):
        """ Now, Let's pytest every object's __str__ output, and check wether they print out the message as we want"""
        polygon1 = Polygon("Triangle", [3, 3, 3])
        polygon2 = Polygon("Square", [4, 4, 4, 4])
        polygon3 = Polygon("Hexagon", [5, 5, 5, 5, 5, 5])
        assert str(polygon1) == "Triangle with sides: [3, 3, 3]"
        assert str(polygon2) == "Square with sides: [4, 4, 4, 4]"
        assert str(polygon3) == "Hexagon with sides: [5, 5, 5, 5, 5, 5]"
        polygon1.set_name("Trapezium")
        polygon1.set_sides([3,3,3,3])
        assert str(polygon1) == "Trapezium with sides: [3, 3, 3, 3]"
        assert str(polygon2) == "Square with sides: [4, 4, 4, 4]"
        assert str(polygon3) == "Hexagon with sides: [5, 5, 5, 5, 5, 5]"

    def test_calc_circumf_square(self):
        """ Verifying the calculation of the circumference of a (Square), with the correct output """
        square = Polygon("Square", [10.0, 10.0, 10.0, 10.0])
        assert pytest.approx(square.calculate_circumference(), 0.01) == 40.0

    def test_calc_circumf_triangle(self):
        """ Verifying the calculation of the circumference of a (Triangle), with the correct output """
        triangle = Polygon("Triangle", [10.0, 9.0, 8.0])
        assert pytest.approx(triangle.calculate_circumference(), 0.01) == 27.0

    def test_calc_circumf_rectangle(self):
        """ Validating the calculation of the circumference of a (Rectangle), with the correct output """
        rectangle = Polygon("Rectangle", [10.0, 7.0, 10.0, 7.0])
        assert pytest.approx(rectangle.calculate_circumference(), 0.01) == 34.0

    def test_calc_circumf_pentagon(self):
        """ Validating the calculation of the circumference of a Irregular polygon (Pentagon) """
        pentagon = Polygon("Pentagon", [5.0, 5.0, 5.0, 5.0, 5.0])
        assert pytest.approx(pentagon.calculate_circumference(), 0.01) == 25.0


if __name__ == "__main__":
    pytest.main()
