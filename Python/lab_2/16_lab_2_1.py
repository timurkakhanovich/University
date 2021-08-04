from math import sqrt

class Vector:
    def __init__(self, coord):
        self.vector = coord

    # Add two vectors.  
    def __add__(self, other):
        if len(self.vector) == len(other.vector):
            return Vector(list(map(sum, zip(self.vector, other.vector))))
        else:
            print("You are not allowed to add to different vectors!")
            raise ValueError

    # Subtract two vectors.  
    def __sub__(self, other):
        if len(self.vector) == len(other.vector):
            return Vector(list(map(lambda x, y: x-y, self.vector, other.vector)))
        else:
            print("You are not allowed to subtract to different vectors!")
            raise ValueError

    # Multiply a vector by scalar.  
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([i*other for i in self.vector])
        else:
            if len(self.vector) == len(other.vector):
                return Vector(sum([x*y for x, y in zip(self.vector, other.vector)]))
            else:
                print("You are not allowed to use scalar mult for different vectors!")
                raise ValueError

    def __rmul__(self, other):
        return Vector([i*other for i in self.vector])
    
    # Equality.  
    def __eq__(self, other):
        return self.vector == other.vector

    # The module of the vector.  
    def module(self):
        return sqrt(sum(list(map(lambda x: x**2, self.vector))))

    def __getitem__(self, index):
        return self.vector[index]

    def __str__(self):
        return str(self.vector)

def main():
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([1, 2, 3])
    vec3 = Vector([-1, 3, 6])

    print("{} + {} = {};".format(vec1, vec2, vec1 + vec2))
    print("{} - {} = {};".format(vec1, vec3, vec1 - vec3))
    print("{} * {} = {};".format(vec1, 5, vec1 * 5))
    print("{} * {} = {};".format(4, vec2, 4 * vec2))
    print("<{}, {}> = {};".format(vec3, vec1, vec3 * vec1))
    print("Does {} equal {}? - {};".format(vec1, vec3, vec1 == vec3))
    print("Does {} equal {}? - {};".format(vec1, vec2, vec1 == vec2))
    print("Length of the {} is {};".format(vec1, vec1.module()))
    print("{}'th index of the {} is {}.".format(1, vec3, vec3[1]))

if __name__ == "__main__":
    main()
