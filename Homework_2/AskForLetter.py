
def AskForLetter():

        ask = True

        
        input = raw_input('''Enter a single letter:
Enter 'quit' to exit.\n''')
        if input == 'quit':
                ask = False
                        
        while ask == True:
                if input != 'quit' and len(input) == 1:
                        vowel = IsVowel(input)

                if vowel == True:
                        PrintIsVowel(input)
                        # ask = False
                                
                if vowel == False:
                        PrintIsNotVowel(input)
                ask = False       
                                        


def IsVowel(letter):

# test whether letter is lowercase vowel

        lowercase = IsLowerCaseVowel(letter)

# test whether letter is uppercase vowel

        uppercase = IsUpperCaseVowel(letter)

        if lowercase == True or uppercase == True:
                return True
        else:
                return False

def IsLowerCaseVowel(letter):

#compare input letter to see if it's a lowercase vowel
        
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                print 'Function IsLowerCaseVowel: letter is lower case and is a vowel'
                return True
        else:
                print 'Function IsLowerCaseVowel: letter is either NOT lower case or NOT a vowel'
                return False

def IsUpperCaseVowel(letter):

# compare input letter to see if it's an uppercase vowel
        
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                print 'Function IsUpperCaseVowel: letter is upper case and is a vowel'
                return True
        else:
                print 'Function IsUpperCaseVowel: letter is either NOT upper case or NOT a vowel'
                return False



def PrintIsVowel(letter):
        print "The letter entered, " + letter + ", is a vowel."

def PrintIsNotVowel(letter):
        print "The letter entered, " + letter + ", is NOT a vowel." 

# def Run():
#        AskForLetter()
# if __name__=='__main__':
#        Run()

        
