import json

def check_type(obj):
    if isinstance(obj, bool):
        return bool_to_json(obj)
    elif isinstance(obj, (int, float)):
        return num_to_json(obj)
    elif isinstance(obj, str):
        return str_to_json(obj)
    elif isinstance(obj, (list, tuple)):
        return list_to_json(obj)
    elif isinstance(obj, dict):
        return dict_to_json(obj)
    elif obj is None:
        return none_to_json(obj)
    else: 
        raise ValueError

def num_to_json(el):
    return el

def str_to_json(el):
    string = ['\"']
    string.append(el + '\"')

    return ''.join(string)

def list_to_json(el):
    new_list = []
    for obj in el:
        new_list.append(check_type(obj))   

    # Fixing problems with \ - literals.  
    new_list = str(new_list).replace('\\', '')
    new_list = new_list.replace('\'', '')

    return new_list

def bool_to_json(el):
    el = str(el)

    el = el.replace('True', 'true')
    el = el.replace('False', 'false')

    return el

def none_to_json(el):
    return str(el).replace('None', 'null')

def dict_to_json(el):
    new_dict = dict()

    # Change key format.  
    for key in el.keys():
        if isinstance(key, (int, float)):
            new_key = str(key)
            new_dict[new_key] = el[key]
        else:
            new_dict[key] = el[key]

    # Change value of key format.  
    for key in new_dict.keys():
        new_dict[key] = check_type(new_dict[key])
    
    # Extra-symbols handling.  
    new_dict = str(new_dict).replace('\'', '\"')
    new_dict = new_dict.replace('\""', '\"')
    new_dict = new_dict.replace('\"[', '[')
    new_dict = new_dict.replace(']\"', ']')
    new_dict = new_dict.replace('\"true\"', 'true')
    new_dict = new_dict.replace('\"false\"', 'false')
    new_dict = new_dict.replace('\"null\"', 'null')

    return new_dict

def to_json(obj):
    iter_data_list = [obj]
    json_content = []

    for data in iter_data_list:
        json_content.append(check_type(data))
    
    return ''.join(json_content)

def main():
    x = [1, 2, 'hello', {
    1: 'John',
    'age': 30.5,
    'city': 'New York',
    'hobbies': ('tennis', 'poker', 'swimming'),
    'he': None,
    'it': True
    }]
    
    myList = [1, [2, [False, ('yep', 'eyah')]], 'hi', None, True]

    print(to_json(myList))
    print(json.dumps(myList))

    print(to_json(x))
    print(json.dumps(x))

if __name__ == "__main__":
    main()
