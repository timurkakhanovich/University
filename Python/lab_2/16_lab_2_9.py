class Value:
    def __get__(self, obj, cls):
        return obj.sum

    def __set__(self, obj, value):
        obj.sum += value*(1 - obj.commission)
        print("The sum in the account is {}.".format(obj.sum))

class Account:
    def __init__(self, commission):
        self.sum = 0
        self.commission = commission

    val = Value()

def main():
    account = Account(0.04)

    account.val = 5
    account.val = 12

if __name__ == "__main__":
    main()
