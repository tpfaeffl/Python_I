'''
homework_3.py
author: Thomas Pfaeffle

This is a program that asks the user to enter a three word phrase and
returns the phrase in pig latin. If words != 3, the program exits. If
'quit' is entered, the program stops.

'''

def LowercaseSentence(sentence):
    # print "calling LowerCaseSentence function"
    sentence = sentence.lower()
    # print "lower case: ", sentence, "\n"
    return sentence

def SplitSentencetoList(sentence):
    # print "calling SplitSentence function"
    sentence = sentence.split()    
    if len(sentence) != 3:
        print "the number of words is", len(sentence)
        print "The number of words must be exactly 3. Exiting"
        exit()
    # print "split to list", sentence, "\n"
    return sentence


def ConvertWordToPigLatin(sentence):
    # print "calling ConvertToPigLatin function \n"
    sentence2 = []
    for value in sentence:
        original_word = value 
        first_letter = original_word[:1]
       # print value, first_letter
    
        if first_letter in GLOBAL_VOWEL_LIST:
            new_word=value+"hay"
            # print "This is the new_word with vowel: ", new_word
            sentence2.append(new_word)
        else:
            new_word=value[1:]+value[:1]+"ay"
            # print "This is the new_word without vowel: ", new_word
            sentence2.append(new_word)
            
    # print "this is the new sentence", sentence2, "\n"
    return sentence2

def PrintThreeWordPhrase(sentence):
    # print "calling PrintThreeWordPhrase \n"
    print "Your phrase in Pig Latin is: ", sentence, "\n"


# main
GLOBAL_VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']

ask = True
while ask == True:
    input_phrase = raw_input('''Enter a three word phrase without punctuation. 
Enter 'quit' to exit.\n''')
    # print len(input_phrase)
    if input_phrase == 'quit':
        ask = False
    else:
        lower_case = LowercaseSentence(input_phrase)
        split_phrase = SplitSentencetoList(lower_case)
   #     if len(input_phrase)!=3:
   #         print "the number of words is", len(input_phrase)
   #         print "The number of words must be exactly 3. Exiting"
   #         ask = False
   #     else:
        sentence3 = ConvertWordToPigLatin(split_phrase)
        PrintThreeWordPhrase(sentence3)

