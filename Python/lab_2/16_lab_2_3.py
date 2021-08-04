class Logger:
    def __init__(self):
        self.result = []
    
    @staticmethod
    def log(func):
        def get_method_data(self, *args):
            self.result.append({"function": func.__name__, "args": args, "result": func(self, *args)})

        return get_method_data

    def __str__(self):
        str_format = "{}\n" * (len(self.result) - 1) + "{}"

        return str_format.format(*self.result)

class Operations(Logger):
    @Logger.log
    def addit(self, *args):
        return sum(args)

    @Logger.log
    def pow(self, *args):
        return list(map(lambda x: x**2, args))

    @Logger.log
    def say_hello(self):
        print("Hello")

    def __str__(self):
        return super().__str__()

def main():
    opers = Operations()
    
    opers.pow(2, 3, 4)
    opers.addit(1, 2, 3)
    opers.addit(10, 20, 100)
    opers.say_hello()
    
    print(opers)

if __name__ == "__main__":
    main()
