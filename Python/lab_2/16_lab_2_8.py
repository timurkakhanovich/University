def singleton(this_class):
    instances = {}

    def called(*args):
        # Check if the instance of this class exists.  
        if this_class.__name__ not in instances.keys():
            instances[this_class.__name__] = this_class(*args)

        return instances[this_class.__name__]
    
    return called

@singleton
class Operations:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "Class: {}. Attributes: {}".format(self.__class__.__name__, tuple(self.__dict__.values()))

def main():
    a = Operations(1, 4)
    b = Operations(2, 5)

    print(a)
    print(b)

if __name__ == "__main__":
    main()
