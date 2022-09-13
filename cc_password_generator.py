"""
generate_password() function generates a passphrase depending on the length specified i.e. word_count. 
i used diceware wordlist that i converted to a dictionary and used that dictionary to randomly select words from the dictionary
"""



from cc_save_retrieve_dictionary import *
import random

def create_passwords_dictionary_from_text_file(text_file='diceware-word-list.txt'):
    try:
        with open(text_file, 'r') as file:
            all_words = file.read().split()
            diceware_dict = dict()
            
            print('Generating Dictionary ....')
            for i in range(0, len(all_words), 2):
                diceware_dict[f'{all_words[i]}'] = all_words[i+1]

            print('Saving Dictionary to Json ....')
            write_dictionary_to_a_file(dictionary_object=diceware_dict, file_path='diceware-dictionary.json')
            print('Dictionary Saved as "diceware-dictionary.json"')
    except:
        print(e)

def generate_password(word_count=5):
    password_number_list = list()

    for i in range(word_count):
        pass_number = ''
        for j in range(5):
            pass_number += str(random.randint(1,6))
        password_number_list.append(pass_number)
    
    # load json into dictionary and check if the password_number exists in the dictionary
    diceware_dict = read_dictionary_from_a_file(file_path='diceware-dictionary.json')
    password = []
    for num in password_number_list:
        if num in diceware_dict.keys():
            phrase = diceware_dict.get(num)
            password.append(phrase)
    return ' '.join(word for word in password)



if __name__ == '__main__':
    # generating dictionary from diceware word list and saving it as a json


    # create_passwords_dictionary_from_text_file()


    # generate password_numbers
    print(generate_password(8))
