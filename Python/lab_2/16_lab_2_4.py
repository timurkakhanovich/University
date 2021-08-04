class default_dict(dict):
    def __init__(self):
        self.d = 0

    def __setitem__(self, key, value):
        self.check_default()

        self.d[key] = value

    def __getitem__(self, key):
        self.check_default()

        try:
            return self.d[key]
        # If key wasn't found.  
        except KeyError:
            self.d[key] = default_dict()

        return self.d[key]

    def __repr__(self):
        """
        We use __repr__ instead of __str__ to show all nested dicts in the class.  
        """
        return str(self.d)
    
    def check_default(self):
        if isinstance(self.d, int):
            self.d = {}

def main():
    d = default_dict()

    d["a"]["b"]["c"]["d"]
    print(d)
    d["a"]["b"]["c"] = 1
    print(d)
    
if __name__ == "__main__":
    main()
