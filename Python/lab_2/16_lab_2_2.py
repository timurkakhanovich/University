class MetaAttr(type):
    def __new__(Class, classname, supers, classdict):
        privates = [(name, value) for name, value in classdict.items()
                                     if name.startswith("private_")]
        public = [(name, value) for name, value in classdict.items() 
                                    if name.startswith("public_")]
        protected = [(name, value) for name, value in classdict.items() 
                                    if name.startswith("protected_")]

        other = dict([(name, value) for name, value in classdict.items() 
                                        if not name.startswith(("private_", 
                                                                "public_", 
                                                                "protected_"))]) 

        to_private = dict((name.replace("private_", "_{}__".format(classname), 1), value) 
                            for name, value in privates)
        to_public = dict((name.replace("public_", "", 1), value) 
                            for name, value in public)
        to_protected = dict((name.replace("protected_", "_{}_".format(classname), 1), value) 
                            for name, value in protected)
        
        other = dict(**other, **to_private, **to_public, **to_protected)

        print("\nAn old classdict:\n{}".format(classdict))
        print("\nA new classdict:\n{}\n".format(other))

        return type.__new__(Class, classname, supers, other)

class Addition(metaclass=MetaAttr):
    private_a = 5
    private_b = 6
    public_c = 7
    public_d = 8
    protected_e = 9
    protected_f = 10
    
    def addit(self):
        return self.__a + self.__b

def main():
    add = Addition()

    print("The result is {}".format(add.addit()))

    print(add.c)

    # Attribute error.  
    #print(add.a)

if __name__ == "__main__":
    main()
