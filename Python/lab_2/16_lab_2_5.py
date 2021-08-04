def cached(func):
    func_data = []

    def write_result(*args):
        is_unique = True

        for data in func_data:
            if func.__name__ == data["func"] and args == data["args"]:
                print("Repeated result is {}.".format(data["res"]))
                is_unique = False

        if is_unique:
            func_data.append({"func": func.__name__, "args": args, "res": func(*args)})
            print("Result is {}.".format(func(*args)))

    return write_result

@cached
def addit(*args):
    return sum(args)

@cached
def to_pow(*args):
    return list(map(lambda x: x**2, args))

def main():
    addit(1, 2, 3, 4)
    addit(1, 2, 3, 4)
    addit(4, 3, 2, 1, 10)
    to_pow(7, 8, 9)
    to_pow(3, 4, 5)
    to_pow(7, 8, 9)

if __name__ == "__main__":
    main()
    