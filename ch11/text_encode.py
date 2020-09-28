if __name__ == '__main__':
    with open('2.txt', 'r') as f:
        text_list = []
        for text in f.readlines():
            text_list.append(text.strip())
        print(''.join(text_list))
