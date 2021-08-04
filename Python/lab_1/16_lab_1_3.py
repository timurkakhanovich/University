import argparse

def division(num):
    divisor = 3
    list_of_factors = []

    # We check if num is divided by 2 at first.  
    while num % 2 == 0:
        num /= 2
        list_of_factors.append(2)

    while num > 1:
        # We check if the number is divided by divisor.  
        while num % divisor == 0:
            num /= divisor
            list_of_factors.append(divisor)
        divisor += 2

    return list_of_factors

def main():
    parser = argparse.ArgumentParser(description='Getting the number')
    parser.add_argument('-N', '--num', type=int, help='Number')

    args = parser.parse_args()

    if args.num is not None:
        number = args.num
    else:
        number = int(input("Enter the number: "))

    print("The list of factors is {lst}".format(lst=division(number)))

if __name__ == "__main__":
    main()
