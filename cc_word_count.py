




def get_word_count(file_path='lorem.txt'):
    try:
        with open(file_path, 'r') as file:
            words = dict()
            content =  file.read().split(' ')
            for word in content:
                if word.upper() in words:
                    words[word.upper()] += 1
                else:
                    words[f'{word.upper()}'] = 1
            top = [word for word in words.keys() if words.get(word) >= 3]
            print(f""" 
            Total Words : {len(content)} \n
            Top 20 words: {top} 
            """)

    except Exception as e:
        print('exception')
        print(e)

        
if __name__ == '__main__':
    get_word_count()