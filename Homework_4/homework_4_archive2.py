'''
homework_4.py
Author: Thomas Pfaeffle
'''

def AskForNumberCities():
    '''Asks user for the number of cities he wants to visit
'''
    print"Calling AskForNumberCities\n\n"
    num_cities = raw_input("How many cities to you want to visit? ")
    # i = int(i)
    # print num_cities, type(i)
    return num_cities

def AskForCityName(i):
    '''Asks for the names of cities. Number of names should be equal to
i. There should be no duplicates in the list.
'''
    print "\n\nCalling AskForCityName\n"
    i = int(i)
    city_names = []
    
    
    # city_names = city_names[]
    for j in range(0, i, 1):
        
      #  print "counter j = ", j
        city_name = raw_input("\nEnter the names of cities: ")
        # city_name = input_city
        if city_name in (city_names):
            print ("\nYou entered a duplicate. Choose different city\n")
          #  print "j=j-1 value: ", j
             # break
            continue
        else:
            city_names.append(city_name)
            print city_names
        
        # continue
    city_names_string = ' '.join(city_names)
    
    print '\n', city_names_string
    return city_names

def PrintFirstCitySentence(list1):
    '''This function prints a sentence listing your first three destinations
'''
    print "\nCalling PrintFirstCitySentence \n\n"
    # print "Type of list1 is: ", type(list1)
    phrase1 = []
    phrase2 = []
    phrase3 = []
    # phrase_full= []

    for i, item in enumerate(list1):
        if i == 0:
            phrase1 =['You would like to visit', item, 'as city', str(i+1) ]
            # print phrase1
        elif i == 1:
            phrase2 =[' and', item, 'as city' , str(i+1)]
            # print phrase2
        elif i == 2:
            phrase3 =[' and', item, 'as city' , str(i+1) , 'on your trip. ']
            # print phrase3
        else:
            None


    phrase1_string=' '.join(phrase1)
    phrase2_string=' '.join(phrase2)
    phrase3_string=' '.join(phrase3)

    # print phrase1_string, phrase2_string, phrase3_string
    phrase_full = phrase1_string + phrase2_string + phrase3_string
    print phrase_full, "\n\n"
    return phrase_full

def PrintAddOneCityNumSentence(phrase_full):
    '''This function adds 1 to the city number'''
    print "Calling PrintAddOneCityNumSentence \n\n"
    list2=[]
    list1 = phrase_full.split()
    # print list1
    for i, item in enumerate(list1):
        if item.isdigit() == False:
         #   print item
            list2.append(item)
         #   print list2
            continue
        else:
            new_city_num = int(item) + 1 
            new_city_name_string = str(new_city_num)
            list2.append(new_city_name_string)

    # print list2
    string2 = " ".join(list2)
    print string2
    
# main

i=AskForNumberCities()
city_names=AskForCityName(i)
phrase_full=PrintFirstCitySentence(city_names)
PrintAddOneCityNumSentence(phrase_full)

