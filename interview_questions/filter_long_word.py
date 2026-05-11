# Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.

def filter_long_words(word_list: list, length: int) -> any:
    for i in word_list:
        if len(i) > length :
            print(i, end = ' ')

word_list = ['a', 'ab','abc','abcdef','four','three']

filter_long_words(word_list,int(input('enter length : ')))
