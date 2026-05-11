# Write a function find_longest_word() that takes a list of words and returns the length of the longest word and that word itself.

def find_longest_word(word_list):
    maximum = 0

    for i in word_list:
        if len(i) > maximum:
            maximum = len(i)
        else:
            continue
        
    print(maximum)

word_list = ['a', 'ab','abc','abcdef','four','three']

find_longest_word(word_list)
