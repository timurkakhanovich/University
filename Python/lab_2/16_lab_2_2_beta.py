class Private:
    def __setattr__(self, attr, value):
        # Check if attribute is in the subclasses.  
        for vars in self.__class__.__bases__:
            if attr in vars().__dict__.keys():
                raise AttributeError 

        if attr in self.__dict__.keys():
            raise AttributeError
        else:
            self.__dict__[attr] = value

class Public:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value

class Protected:
    def __setattr__(self, attr, value):
        if attr in self.__dict__.keys():
            raise AttributeError
        else:
            self.__dict__[attr] = value  

# Private class.  
class Addition(Private):
    def __init__(self):
        self.a = 40
        self.b = 50
    
    def add(self):
        return self.a + self.b

# Public.  
class Multiplication(Public):
    def __init__(self):
        self.num1 = 5
        self.num2 = 8

    def mult(self):
        return self.num1 * self.num2

# Inheritance (Protected).  
class Addition_inh(Protected):
    def __init__(self):
        self.a0 = 40
        self.b0 = 50
    
    def add(self):
        return self.a0 + self.b0

class Multiplication_inh(Addition_inh):
    def __init__(self):
        self.a0 = 5
        self.b0 = 8 

    def mult(self):
        return self.a0 * self.b0 

def main():
    addition = Addition()
    multiplication = Multiplication()
    inh_multiplication = Multiplication_inh()

    #addition.b = 50     # Trying to change private attribute. Error.  
    multiplication.num1 = 6     # Changing public attribute.  

    print(addition.add())
    print(multiplication.mult())

    #inh_multiplication.a0 = 6
    print(inh_multiplication.mult())

if __name__ == "__main__":
    main()
