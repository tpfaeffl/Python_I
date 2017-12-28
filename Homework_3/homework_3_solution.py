'''
homework_3_solution.py
'''

#  General requirements with point values:
#  Points:                                                            pts. off if corrected       pts. off if not corrected
#  1.  Violation of style guide                                               0                            5
#  2.  Very Confusing Code                                                    0                            5
#  3.  Define global VOWELS list                                              1                            2
#  4.  Ask user for 3 word phrase and spaces                                   2                            3
#  5.  Convert input from string to list in SplitSentenceIntoList               2                            3
#  6.  Convert list elements to pig latin by calling ConvertWordToPigLatin       2                            3
#  7.  Function to read user input (AskUserForSentence)                         2                            3
#  8.  Function to lowercase the sentence/word (LowercaseSentence)              2                            3
#  9.  Function that splits phrase (SplitSentenceIntoList)                      2                            3
#  10. Function that prints out converted phrase (PrintThreeWordPhrase)         2                            3
#  11. Script continues until quit                                             2                            3
#  12. Correct usage of brackets and ranges when getting sub-string              2                            4
#  13. Have check to verify phrase input has length of 3                        1                            2

LOWERCASE_VOWELS_LIST = ['a', 'e', 'i', 'o', 'u']


def AskUserForSentence():
    """ Return a phrase given by the user."""

    sentence = raw_input('Input a 3 word phrase with spaces to convert to Pig latin.  Type "quit" to end: ')
    return sentence
            

def LowercaseSentence(sentence):

    return sentence.lower()


def SplitSentenceIntoList(sentence):

    word_list = sentence.split()

    return word_list

def ConvertWordToPigLatin(word):

    if word[0] in LOWERCASE_VOWELS_LIST:
        pig_latin_word = word + 'hay'
        return pig_latin_word
    
    elif word[0] not in LOWERCASE_VOWELS_LIST:
        pig_latin_word = word[1:] + word[0] + 'ay'
        return pig_latin_word
    
    else:
        return None

def PrintThreeWordPhrase(one, two, three):

    print one, two, three


def Run():

    while True:
        sentence = AskUserForSentence()
        if sentence == 'quit':
            break
        else:
            lower_sentence = LowercaseSentence(sentence)
            word_list = SplitSentenceIntoList(lower_sentence)
            if len(word_list) == 3:
                # we do not know for loops yet, so we can make
                # 3 separate calls to ConvertWordToPigLatin
                pig_latin_word_1 = ConvertWordToPigLatin(word_list[0])
                pig_latin_word_2 = ConvertWordToPigLatin(word_list[1])
                pig_latin_word_3 = ConvertWordToPigLatin(word_list[2])
                PrintThreeWordPhrase(pig_latin_word_1, pig_latin_word_2, pig_latin_word_3)

Run()

