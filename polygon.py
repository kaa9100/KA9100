class Polygon:

    def __init__(self,name,sides):
        self.name = name
        self.sides = sides
    
    def get_name(self):
        """ We've created an Accessor, in order to get / fetch the name of a specific object if needed! """
        return self.name
    
    def set_name(self,new_name):
        """ We've created an Mutator, in order to mutate / change the name of a specific object if needed! """
        self.name = new_name

    def get_sides(self):
        """ We've created an Accessor, in order to get / fetch the sides of a specific object if needed! """
        return self.sides
    
    def set_sides(self,new_sides):
        """ We've created an Mutator, in order to mutate / change the sides of a specific object if needed! """
        self.sides = new_sides
    
    def __str__(self):
        """ Let's use now the special method __str__, in order to create a readable message for the user """
        return self.name +" with sides: "+ str(self.sides)
    
    def calculate_circumference(self):
        return sum(self.sides) if self.sides else 0.0
    
    def __eq__(self, other):
        """ Let's use the special method __eq__, in order to check that the two object have the same type,name and sides """
        if type(self) == type(other):
            return self.name == other.name and self.sides == other.sides
        else:
            return False
    
    def __ne__(self, other):
        """ Let's use the special method __ne__, which corresponds to __eq__ and checks the inequality between the objects """
        return not self.__eq__(other)
    


def main():
    polygon1=Polygon("Triangle",[3,3,3])
    polygon2=Polygon("Square",[4,4,4,4])
    polygon3 = Polygon("Hexagon",[5,5,5,5,5,5])
    print(polygon1)
    print(polygon2)
    print(polygon3)
    print("The circumference of Polgyon1 (Triangle) is:",polygon1.calculate_circumference())
    print("The circumference of Polgyon2 (Square) is:",polygon2.calculate_circumference())
    print("The circumference of Polgyon3 (Hexagon) is:",polygon3.calculate_circumference())
    print(polygon1.get_name())
    print(polygon1.get_sides())
    polygon1.set_name("trapezium")
    polygon1.set_sides([3,3,3,3])
    print(polygon1)
    print(polygon1 == polygon2)
    print(polygon1 != polygon2)

if __name__ == "__main__":
    main()
