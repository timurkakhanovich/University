class Filter:
    def __init__(self, iterable, func=True, stop=40):
        self.iterable = iterable
        self.current = iter(iterable)
        self.Filter = func
        self.pos = 0
        self.stop = stop

    def __iter__(self):
        self.current = iter(self.iterable)
        self.pos = 0
        return self
    
    def __next__(self):
        if self.pos != self.stop:
            return self.suitable_next()
        else:
            raise StopIteration

    def suitable_next(self):
        # do while loop.  
        check = False
        while not check:
            try:
                c = next(self.current)
            except StopIteration:
                self.current = iter(self.iterable)
                c = next(self.current)

            # Check if there were no filter function.  
            if isinstance(self.Filter, bool):
                check = self.Filter
            else:
                check = self.Filter(c)

        self.pos += 1
        return c

def evenQ(x):
    return x % 2 == 0

def main():
    f = Filter(range(10), func=evenQ, stop=35)
    s = Filter(range(30))

    print([i for i in f])
    x = iter(s)
    print(next(x), next(x), next(x))
    print([i for i in s])

if __name__ == "__main__":
    main()
