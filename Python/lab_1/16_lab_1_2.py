# String input.  
def get_string():
    string = input("Enter a string: ")
    string = string.lower()

    # Deleting spare words so that words in the string will be unique.  
    string = ' '.join(list(set(string.split())))
    return string

# Get words amount.  
def words_amount(string):
    return string.count(' ') + 1

def print_comb_list(string, index_arr):
    list_comb = []
    for i in index_arr:
        list_comb.append(string[i])

    print(' '.join(list_comb))

def combination(string, k):
    length = words_amount(string)
    index_arr = list(range(k))
    string = string.split()
    up_limit = k - 1

    while index_arr[0] != length - k:
        print_comb_list(string, index_arr)

        # Check if the last index is equal to its index limit.  
        if index_arr[up_limit] == length - 1:
            for pos in range(k):
                # Check if some index is equal to its pos limit.   
                if index_arr[pos] == length - k + pos:
                    # Then we increment the previous index.  
                    index_arr[pos - 1] += 1
                    add_param = 1
                    for up_it in range(pos, up_limit + 1):
                        # Initializing the other indexes according to their position and rise them on add_param.  
                        index_arr[up_it] = index_arr[pos - 1] + add_param
                        # add_param will be changed with each iteration.  
                        add_param += 1
                    # We decrement the last index because it'll be incremented then in the main loop.  
                    index_arr[up_limit] -= 1
                    break 

        index_arr[up_limit] += 1

    # Printing the last combination.  
    print_comb_list(string, index_arr)
            
def show_the_result_even_combinations(string):
    length = words_amount(string)
    
    for it in range(2, length + 1, 2):
        print("{pos} combination: ".format(pos=it))
        combination(string, it)

def main():
    string = get_string()
    show_the_result_even_combinations(string)

if __name__ == "__main__":
    main()
