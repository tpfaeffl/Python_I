
ask = True

while ask == True:
        input = raw_input('''Please input a single letter:
Type 'quit' to end.\n''')
        if input == 'quit':
            ask = False
        else:    
            letter = input


# IsUppercase test
# Takes as input a single charater string and
# returns True if character string is uppercase vowel.

        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            result = 'vowel is uppercase'
            response1 = 'true'
            print result
            # return True
        else:
            result = 'vowel is not uppercase'
            response1 = 'false'
            print result
            # return False


# IsLowerCase test
# Will take as input a single charater string and return 
# True is character string is lowercase vowel.

        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            result2 = 'vowel is lowercase'
            response2 = 'true'
            print result2
            # return True
        else:
            result2 = 'vowel is not lowercase'
            response2 = 'false'
            print result2
            
            # return False
            
# Print the result
        if response1 == 'true' or response2 == 'true':
                print "The letter " + letter + " originally input is a vowel."
        else:
                print "The letter " + letter + " originally input is NOT a vowel."
