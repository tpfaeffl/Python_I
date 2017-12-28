GLOBAL_VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']

sentence = ['boot', 'cat', 'image']
sentence2 = []

print sentence

for value in sentence:
    original_word = value 
    first_letter = original_word[:1]
    # print value, first_letter
    
    if first_letter in GLOBAL_VOWEL_LIST:
        new_word=original_word+"hay"
      #  print new_word
        sentence2.append(new_word)
    else:
        new_word=original_word[1:]+original_word[:1]+"ay"
      #  print new_word
        sentence2.append(new_word)
        
print "this is the new sentence", sentence2

