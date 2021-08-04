from collections import defaultdict
import argparse

def getString():
    """
    This function reads the text from file,  
    clears the text from spare lexems and returns the list of words.  
    """

    with open(r'text_files/in_7.txt', 'r', encoding='UTF-8') as inp:
        string = inp.read().lower()

    # Clear the string from lexems.  
    return delete_lexems(string, [ '?', '!', ',', ':', ';', '(', ')', '\"', '\'', '\n'])
    
def delete_lexems(string, lexems):
    """
    String with lexems -> list of words of the string without lexems.  
    ? ! -> . 
    endl -> space.    
    """
    string = ' '.join(string.split())

    for symb in lexems:
        if symb is '?' or symb is '!':
            string = string.replace(symb, '.')
        else:
            string = string.replace(symb, '')

    return string.split()

def get_amount_of_words_statistic():
    """
    Returns dict of words.  
    """
    words_list = getString()
    # Clear the string from lexems of the end of sentence.  
    words_list = delete_lexems(' '.join(words_list), ['.'])
    
    words_repeat_stat = defaultdict(int)

    for word in words_list:
        words_repeat_stat[word] += 1
    
    return words_repeat_stat

def print_amount_of_words(words_stat):
    """
    Input: statistic of words repeating (type = dict).  
    This function write a word and how many times it meets in the text.  
    """

    with open(r'text_files/out_7.txt', 'w', encoding='UTF-8') as output:
        output.write("1)-------------------------------------------------------------------------\n")
        for word in words_stat.keys():
            output.write("Word {} meets {} times\n".format(word.upper(), words_stat[word]))        

def get_average_statistic():
    # Get the list of sentences.  
    string = ' '.join(getString())
    string = string.split('.')
    sectences_amount = len(string)

    string = ''.join(string).split()
    words_amount = len(string)

    with open(r'text_files/out_7.txt', 'a', encoding='UTF-8') as output:
        output.write("2)-------------------------------------------------------------------------\n")
        output.write("The average amount of words in sentences is {}\n".format(round(words_amount/sectences_amount)))

def get_median_statistic():
    string = ' '.join(getString())
    string = string.split('.')
    # Delete the last empty element.  
    del string[-1]

    # Append a space to the first sentence.  
    string[0] += ' '
    words_amount = []
    for sentence in string:
        words_amount.append(sentence.count(' '))

    # Sorting the dict.  
    words_amount = sorted(words_amount)
    median = 0

    if len(words_amount) % 2 != 0:
        median = words_amount[round(len(words_amount)/2)]
    else:
        median = (words_amount[int(len(words_amount)/2)] + words_amount[int(len(words_amount)/2 - 1)]) / 2

    with open(r'text_files/out_7.txt', 'a', encoding='UTF-8') as output:
        output.write("3)-------------------------------------------------------------------------\n")
        output.write("The median amount of words in sentences is {}\n".format(int(median)))

def getArguments():
    parser = argparse.ArgumentParser("Getting top K of N-gramms")
    parser.add_argument("-K", "--K", type=int, help="Top K")
    parser.add_argument("-N", "--N", type=int, help="N-gramm")

    args = parser.parse_args()
    
    if args.K and args.N:
        return (args.K, args.N)
    else:
        K = int(input("Enter K parameter: "))
        N = int(input("Enter N parameter: "))
        return (K, N)

def get_top_statistic(K=10, N=4):
    words = get_amount_of_words_statistic()
    newWords = {}

    for element in words.keys():
        if len(element) == N:
            newWords[element] = words[element]
    
    newWords = dict(sorted(newWords.items(), key=lambda x: x[1], reverse=True))

    return newWords

def print_top_statistic():
    # Top K.  
    param = getArguments()
    # top_words has type(dict).  
    top_words = get_top_statistic(*param)
    top = 1

    with open(r'text_files/out_7.txt', 'a', encoding='UTF-8') as output:
        output.write("4)-------------------------------------------------------------------------\n")
        for word in top_words.keys():
            # If top reaches its limit we breaks the loop.  
            if top - 1 == param[0]:
                break
            output.write("Top {} is {}. {} times\n".format(top, word.upper(), top_words[word]))
            top += 1

def main():
    statistic_1 = get_amount_of_words_statistic()    # statistic - type=dict.   
    print_amount_of_words(statistic_1)

    get_average_statistic()
    get_median_statistic()
    print_top_statistic()

if __name__ == "__main__":
    main()
