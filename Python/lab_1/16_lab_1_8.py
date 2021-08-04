import re

container = set()

def get_data():
    while 1:
        string = input(">> ")
        string = string.split()

        command = string[0]
        command_samples = ['add', 'remove', 'find', 'list', 'grep', 'save', 'load', 'exit']

        if command in command_samples:
            # String -> int.  
            keys = eval(keys_handling(string))
            return (command, keys)
        else:
            print("Undefined command!")

def keys_handling(string):
    keys_string = ''.join(string[1:])

    for symb in keys_string:
        if symb in ['[', ']', ',']:
            keys_string = keys_string.replace(symb, ' ')
    
    return str(keys_string.split())

def add(key):
    global container

    if isinstance(key, list):
        for el in key:
            container.add(el)
    else:
        container.add(key)

def remove(key):
    global container

    container.discard(key[0])

def find(key):
    found = set()

    if isinstance(key, list):
        for el in key:
            if el in container:
                found.add(el)
    else:
        if key in container:
            found.add(key)
    
    if found == set():
        print(False)
    else:
        print(found)

def _list():
    print(container)

def grep(regexp):
    found = set()

    for elem in container:
        if re.search(regexp[0], elem):
            found.add(elem)
    
    print(found)

def save():
    with open(r'text_files/out_8.txt', 'w', encoding='UTF-8') as output:
        output.write("Result container: " + str(container))

def load():
    global container
    
    with open(r'text_files/in_8.txt', 'r', encoding='UTF-8') as inp:
        string_container = inp.read()
        for symb in string_container:
            # String [1, 2, 3, 4, 5] -> 1,2,3,4,5  
            if symb in ['{', '}', ' ', '[', ']']:
                string_container = string_container.replace(symb, '')
        # Delete ,  
        container = set(string_container.split(','))
                
def program():
    while 1:
        data = get_data()

        if data[0] == 'add':
            add(data[1])
        elif data[0] == 'remove':
            remove(data[1])
        elif data[0] == 'find':
            find(data[1])
        elif data[0] == 'list':
            _list()
        elif data[0] == 'grep':
            grep(data[1])
        elif data[0] == 'save':
            save()
        elif data[0] == 'load':
            load()
        elif data[0] == 'exit':
            break

def main():
    program()

if __name__ == "__main__":
    main()
