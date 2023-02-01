with open('trimushketera.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
    text = text.replace('\n', ' ')
    text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('"', '').replace('(', '').replace(')', '').replace('*', '')
    text = text.lower()
    words = text.split()
    words.sort()
    print(len(words))
    unique_words = list(set(words))
    unique_words.sort()
    print(len(unique_words))
    with open('alphabet_words.txt', 'w', encoding='UTF-8') as file:
        file.write(f'Words: {len(unique_words)}' + '\n')
        file.write(f'Unique words: {len(words)}' + '\n')
        for words in unique_words:
            file.write(words + '\n')
        pass