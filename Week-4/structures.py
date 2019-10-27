'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    my_list = []
    my_list = my_list + [the_list[0]]
    my_list = my_list + [the_list[-1]]
    return my_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    rev = the_list[beginning:end]
    rev.reverse
    return rev


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    for i in range(3):
        the_list.append(index)
        the_list.sort()
    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    word_a = str(word)
    word_b = word[::-1]
    if word_a == word_b:
        return 'This word is palidrome'
    else:
        return 'This word is not palidrome'

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    sentence_a = sentence.lower().strip().replace(" ", "")
    sentence_b = sentence_a[::-1]
    if sentence_a == sentence_b:
        return 'This sentence is peledrome'
    else:
        return 'This sentence is not peledrome'

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentence1, sentence2):
    sentence_a = sentence1.strip().replace(" ","")
    sentence_b = sentence2.strip().replace(" ","")
    sentence_test = sentence_a + sentence_b

    if sentence_test[0] == sentence_a[0].upper() and (sentence_test[-1] == '.' or sentence_test[-1] == '!' or sentence_test[-1] == '?'):
        return 'These sentences meet the preamiters'
    else:
        return 'These sentences fail the perameters'


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    return

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    return
