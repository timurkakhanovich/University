id_set = set()

def flatten_it(lst):
    for it_obj in lst:
        # If list contains another list, we will call this function recursively to get values.  
        if isinstance(it_obj, list):
            # If it is a list we add its address to a set.  
            id_set.add(id(it_obj))
            # If the address of our list equals the address of the element we throw ValueError.   
            if id(lst) in id_set:
                raise ValueError
            else:
                # If it's "good" address we delete it.  
                id_set.discard(id(it_obj))
            for another_it in flatten_it(it_obj):
                yield another_it
        else:
            yield it_obj

def main():
    myList = [1, [2, [3, [[1]]], 1], [4], [7, 10, [2]]]
    #myList = [[[1], [2]]]
    myList += [myList]

    lst = [i for i in flatten_it(myList)]
    print(lst)

if __name__ == "__main__":
    main()
