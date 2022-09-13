"""
This module provides a function to check if a string is a palindrome

a string is a palindrome if it is the same when read backwards i.e "madam i'm adam"

"""
import re
def check_if_it_is_a_palindrome(text):
    try:
        input_string = str(text)
        if len(input_string) <= 0:
            return None
    except Exception as e:
        return None
    # 1 remove white spaces if any
    formatted_input = input_string.split()
    concatenated_string = "".join(formatted_input)
    only_alphabets = ""
    lower_case_string = ''
    reversed_string = ''
    
    if concatenated_string.isalpha():
        only_alphabets = concatenated_string
        lower_case_string = only_alphabets.lower()
        reversed_string = lower_case_string[::-1]
    else:
        for character in concatenated_string:
            if character.isalpha():
                only_alphabets += character
        lower_case_string = only_alphabets.lower()
        reversed_string = lower_case_string[::-1]
    

    return lower_case_string == reversed_string

def is_palindrome(phrase):
    try:
        input_string = str(phrase)
        if len(input_string) <= 0:
            return None
    except Exception as e:
        return None
    forwards = ''.join(re.findall(r'[a-z]+', input_string.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
        

if __name__ == "__main__":
    # testing for no input

    test_cases = [None, '', 'a', 5, '5', 'Madam i\'m Adam', 'Hello Ethel', 'level', 'Go hang a salami - I\'M  A LASAGNA HOG.']
    for test in test_cases:
        print(f'{test} is palindrome : {is_palindrome(test)}')