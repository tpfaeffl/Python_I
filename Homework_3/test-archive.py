

def LowercaseSentence(sentence):
    print "calling LowerCaseSentence to List \n"
    sentence = sentence.lower()
   # print "lower case", sentence
    return sentence

def SplitSentencetoList(sentence):
    print "calling SplitSentence to List \n"
    sentence = sentence.split()
   # print "split to list", sentence
    return sentence


def ConvertWordToPigLatin(sentence):
    print "calling ConvertToPigLatin \n"
    sentence2 = []
    for value in sentence:
        original_word = value 
        first_letter = original_word[:1]
       # print value, first_letter
    
        if first_letter in GLOBAL_VOWEL_LIST:
            new_word=original_word+"hay"
       #     print new_word
            sentence2.append(new_word)
        else:
            new_word=original_word[1:]+original_word[:1]+"ay"
        #    print new_word
            sentence2.append(new_word)
            
   # print "this is the new sentence", sentence2, "\n"
    return sentence2

def PrintThreeWordPhrase(sentence3):
    print "calling PrintThreeWordPhrase \n"
    print "Your phrase in Pig Latin is: ", sentence3, "\n"


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
        input_phrase = LowercaseSentence(input_phrase)
        input_phrase = SplitSentencetoList(input_phrase)
        if len(input_phrase)!=3:
            print "the number of words is", len(input_phrase)
            print "The number of words must be exactly 3. Exiting"
            ask = False
        else:
            sentence3 = ConvertWordToPigLatin(input_phrase)
            PrintThreeWordPhrase(sentence3)

