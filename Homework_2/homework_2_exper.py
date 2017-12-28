'''
homework_2.py
Get a letter and determine if it is a vowel. Quit if you find a
vowel or if you enter 'quit'.
'''

def AskForLetter():

        ask = True

        while ask == True:
                input_letter = raw_input('''Enter a single letter:
Enter 'quit' to exit.\n''')
                if input_letter == 'quit':
                        ask = False
                
                if input_letter != 'quit' and len(input_letter) == 1:
                        vowel = IsVowel(input_letter)

                        if vowel == True:
                                PrintIsVowel(input_letter)
                                ask = False
                                
                        if vowel == False:
                                PrintIsNotVowel(input_letter)
                                ask = True       
                                        


def IsVowel(letter):

# get whether letter is lowercase vowel

        lower_case = IsLowerCaseVowel(letter)

# get whether letter is uppercase vowel

        upper_case = IsUpperCaseVowel(letter)

        if lower_case == True or upper_case == True:
                return True
        else:
                return False

def IsLowerCaseVowel(letter):

#compare input letter to see if it's a lowercase vowel
        
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
              #  print 'Function IsLowerCaseVowel: letter is lower case and is a vowel'
                return True
        else:
              #  print 'Function IsLowerCaseVowel: letter is either NOT lower case or NOT a vowel'
                return False

def IsUpperCaseVowel(letter):

#compare input letter to see if it's an uppercase vowel
        
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
               # print 'Function IsUpperCaseVowel: letter is upper case and is a vowel'
                return True
        else:
               # print 'Function IsUpperCaseVowel: letter is either NOT upper case or NOT a vowel'
                return False



def PrintIsVowel(letter):
        print "\n The letter entered, " + letter + ", is a vowel.\n"

def PrintIsNotVowel(letter):
        print "\n The letter entered, " + letter + ", is NOT a vowel.\n" 

# main

AskForLetter()


        
