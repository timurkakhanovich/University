# Global variable to make block lists.  
block = True

def join_lists(a_list, b_list):
    """Getting sorted merge of two blocks."""
    a_index, b_index = 0, 0
    result = []

    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            result.append(a_list[a_index])
            a_index += 1
        else:
            result.append(b_list[b_index])
            b_index += 1

        if a_index == len(a_list):
            result += b_list[b_index:]
        elif b_index == len(b_list):
            result += a_list[a_index:]

    return result

def merge_sort(lst):
    global block

    if block:
        # Dividing the common lst into blocks.  
        for it in range(0, len(lst), 2):
            if lst[it] > lst[it + 1]:
                lst[it], lst[it + 1] = lst[it + 1], lst[it]
            yield [lst[it], lst[it + 1]]
        block = False

    else:
        # Joining blocked lst.  
        for data in range(0, len(lst), 2):
            joined = join_lists(lst[data], lst[data + 1])
            yield joined

def out_sort(lst):
    """Showing the result."""
    global block

    it = 0
    length = len(lst)
    myList = lst

    while 2**it != length:
        myList = [i for i in merge_sort(myList)]
        print(myList)
        it += 1
    # Make block true to have the opportunity of the other output.  
    block = True

def file_out_sort(lst):
    """Showing the result."""
    it = 0
    length = len(lst)
    myList = lst
    global block

    with open(r'text_files/out_5.txt', 'w', encoding='utf-8') as output:
        while 2**it != length:
            myList = [i for i in merge_sort(myList)]
            output.write(str(myList) + "\n")
            it += 1
    # Make block true to have the opportunity of the other output.  
    block = True

def main():
    lst = [4, 2, 6, 2, 8, 0, 10, 9, 11, 100, 78, 101, 1, 2, 11, 12]
    
    out_sort(lst)
    file_out_sort(lst)
    
if __name__ == "__main__":
    main()
