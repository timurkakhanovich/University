class FieldInitializer(type):
    def __new__(Meta, classname, supers, classdict):
        classdict["__setattr__"] = Meta.__dict__["__setattr__"]

        return super().__new__(Meta, classname, supers, classdict)

    def __setattr__(Class, key, value):
        if key in Class.__dict__.keys():
            if not isinstance(value, type(Class.__dict__[key])):
                try:
                    raise AttributeError
                finally:
                    print("Attribute error as expected!")
        
        Class.__dict__[key] = value

    def __call__(Class, *args, **kwargs):
        try:
            # If class has __init__ method.  
            obj = super().__call__(*args, **kwargs)

            for key, value in kwargs.items():
                obj.__dict__[key] = value
        except:
            # If class doesn't have __init__.  
            obj = Class()
            
            for key, value in kwargs.items():
                obj.__dict__[key] = value
            
        return obj

class A(metaclass=FieldInitializer):
    pass

class B(metaclass=FieldInitializer):
    def __init__(self, a, b, c=5, foo=1):
        self.a = a
        self.b = b

def main():
    a = A(foo=42)
    b = B(1, 2, c=3, foo=4)
    
    a.foo = "hello"
    print(a.foo)
    a.foo = 10
    print(a.foo)
    print(b.a)
    print(b.c)
    #b.a = 5.5
    print(b.foo)

if __name__ == "__main__":
    main()
