"""
This module provides a function to write a dictionary to a file and a function to get the dictionary from a file
"""
import json

def write_dictionary_to_a_file(dictionary_object=dict(), file_path='dictionary.json'):
    if type(dictionary_object) == dict:
        try:
            with open(file_path, 'w') as file:
                if len(dictionary_object) > 0:
                    print('writing a dictionary to a file')
                    file.write(json.dumps(dictionary_object))
        except Exception as e:
            print(e)

def read_dictionary_from_a_file(file_path='dictionary.json'):
    try:
        with open(file_path, 'r') as file:
            return json.loads(file.read())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # testing writing a dictionary
    test_dict = {'name': 'norbert'}
    write_dictionary_to_a_file(test_dict)

    # read from a file
    print(read_dictionary_from_a_file())