'''
retirement.py
a program which asks your dream job and ideal hourly wage. The program calculates your
based on a 40/hr week 
'''

# ask for the dream job and the ideal hourly wage

dream_job = raw_input ('What is your dream job? ')
input_hourly_wage = raw_input ('What is your ideal hourly wage? ')

# test for negative numbers and 0
if float(input_hourly_wage) <=0:
    print input_hourly_wage, 'is not a valid value'
else:
#test for string input
    
    try:
        hourly_wage = float(input_hourly_wage)
    except ValueError:
        print 'The input provided' ,input_hourly_wage, 'is not a valid number'
    else:
        print 'The value provided' ,input_hourly_wage, 'IS a valid number'
        yearly_income = hourly_wage * 40 * 52
        print 'Your annual income is' ,'%.2f' % yearly_income

# get the amount of money in the retirement pot
        input_retirement_money = raw_input ('How much total funds do you want in retirement? ')
        # test for negative numbers and 0
        if float(input_retirement_money) <=0:
            print input_retirement_money, 'is not a valid value'
        else:
# test for negative numbers and 0
            try:
                retirement_money = float(input_retirement_money)
            except:
                print 'The input provided' ,input_retirement_money, 'is not a valid number'
            else:
                print 'The value provided' ,input_retirement_money, 'IS a valid number'
                years_to_save = retirement_money/yearly_income
                print 'It will take' ,round(years_to_save,2), 'years to save retirement funds'
                num = round (years_to_save,2)
                if (num % 2) == 0:
                    print num, 'is an even number'
                else:
                    print num, 'is an odd number'
    



# yearly_wage = hourly_wage * 40 * 52
# print 'Annual income is ' ,yearly_wage



