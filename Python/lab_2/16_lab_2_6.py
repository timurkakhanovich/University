class Range:
    def __init__(self, *args):
        self.first = True

        if len(args) > 3 or len(args) == 0:
            raise TypeError

        # Start.  
        first_neg = False
        if args[0] < 0:
            first_neg = True
        
        self.value = args[0]

        # End.  
        if len(args) > 1:
            self.end = args[1]
        elif len(args) == 1 and first_neg:
            # Second is less than first. Result - [].  
            self.end = self.value - 1
        elif len(args) == 1:
            # range(n), n >= 0.  
            self.end = args[0]
            self.value = 0

        # Step.  
        if len(args) < 3:
            self.step = 1
        elif len(args) == 3:
            if args[2] == 0:
                raise ValueError
            self.step = args[2]
            
    def __iter__(self):
        return self
    
    def __next__(self):
        # We don't need to change the first value.  
        if not self.first:
            self.value += self.step
        else:
            self.first = False

        # Correct limits.  
        if (self.value >= self.end and self.step > 0 or
            self.value <= self.end and self.step < 0):
            raise StopIteration

        return self.value

def iteration_demonstration(*args):
    lst = []
    for i in Range(*args):
        lst.append(i)
    print(lst)

def main():
    iteration_demonstration(10)
    iteration_demonstration(-10)
    iteration_demonstration(1, 7)
    iteration_demonstration(7, 1)
    iteration_demonstration(1, 10, 2)
    iteration_demonstration(8, 2, 2)
    iteration_demonstration(10, 6, -2)

if __name__ == "__main__":
    main()
