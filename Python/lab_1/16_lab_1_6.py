import random as rand
import argparse 

def generate_rubbish(string_amount, words_amount, word_length=0):
    isGenerated = False

    # If a word length equals 0 it will be generated then.  
    if not word_length:
        isGenerated = True

    with open(r'text_files/out_6.txt', 'w', encoding='UTF-8') as output:
        for _ in range(string_amount):
            # Prepare the list of words in a string.  
            string = []

            for _ in range(words_amount):
                # Generating a word length if it necessary.  
                if isGenerated:
                    word_length = rand.randint(1, 15)

                for _ in range(word_length):
                    # Symbol generation.  
                    rand_sym = chr(rand.randint(33, 10001))
                    string.append(rand_sym)

                string.append(" ")

            # Writing got string into file.  
            output.write(''.join(string) + '\n')

def getArguments():
    parser = argparse.ArgumentParser(description='Getting parameters of the rubbish output')
    parser.add_argument('-N', '--strAmount', type=int, help='The number of strings')
    parser.add_argument('-K', '--wordsAmount', type=int, help='The amount of words')
    parser.add_argument('-L', '--wordLength', type=int, help='The length of the words')

    args = parser.parse_args()

    # If length is not defined we won't return it.  
    if args.wordLength is None:
        return (args.strAmount, args.wordsAmount)
    else:
        return (args.strAmount, args.wordsAmount, args.wordLength)

def main():
    generate_rubbish(*getArguments())
            
if __name__ == "__main__":
    main()
