"""
This function takes in a list and a number and finds the indices of that number in a list
Python lists can contain other lists, so the function should be able to go deeper into those lists to find the indices
"""

def find_indices(input_list, item):
    indices = list()
    source = input_list
    for idx, list_item in enumerate(source):
        if type(list_item) == list:
            indices.append([idx] + find_indices(list_item, item))
        else:
            if list_item == item:
                indices.append(idx)
    return indices


if __name__ == '__main__':
    print('Testing Function find_indices()')

    print(find_indices([[2,5,[1,2],2],5,[2,3,4,2],2,3,2],2))