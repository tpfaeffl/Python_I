'''
Homework_1.py
Write a program that asks the user for their dream job title.  Then ask
them for the hourly wage they want to earn.  This number should account
for dollars and cents.  Calculate the annual wage they will earn over a
year.  Assume they work 48 weeks a year (4 weeks vacation) but are paid
over 52 weeks.  Then ask them how much money they feel they will need
at retirement time.  Determine the number of years they will have to
work to save up their retirement dollar value assuming their only source
of income was their paycheck?  Finally, determine if the number of years
they need to save is an even or odd number.  For this part, use the modulus
operator to determine if the number you calculated is odd or even.  Once
you have calculated it, use print to print out the value.  You should
also print out something like this.  "If the value is --- then the number
is odd, however, if the value is ----- then the number is even."


'''

# ask for the dream job and the ideal hourly wage

dream_job = raw_input ('What is your dream job? ')
input_hourly_wage = raw_input ('What is your ideal hourly wage? ')

# test wage for negative numbers and 0


    
# test hourly wage for string input
    
try:
    hourly_wage = float(input_hourly_wage)
    if float(input_hourly_wage) <=0:
        print input_hourly_wage, 'is not a valid value'
    else:  
        except ValueError:
            print 'The value provided' ,input_hourly_wage, 'is not a valid number'
        else:
            print 'The value provided' ,input_hourly_wage, 'IS a valid number'

# worker works 48 weeks/year, no paid vacation. Payment spread over 52 weeks.
# calculate weekly and yearly income

        yearly_income = hourly_wage * 40 * 48
        weekly_income = yearly_income / 52
        print ' '
        print '''The worker works hourly for 48 weeks/year with no paid vacation.
However, payment spread over 52 weeks.
'''
        
        print 'Your weekly income is' ,'%.2f' % weekly_income
        print 'Your annual income is' ,'%.2f' % yearly_income
        print ' '

# get the amount of money in the retirement pot

        input_retirement_money = raw_input ('How much total funds do you want in retirement? ')

# test retirement money for negative numbers and 0

        if float(input_retirement_money) <=0:
            print input_retirement_money, 'is not a valid value'
        else:
            
# test retirement money for string input

            try:
                retirement_money = float(input_retirement_money)
            except:
                print ' '
                print 'The input provided' ,input_retirement_money, 'is not a valid number'
            else:

# Print retirement money. Calculate how many years to save it.

                print ' '
                print 'The value provided' ,input_retirement_money, 'IS a valid number'
                years_to_save = retirement_money/yearly_income
                print ' '
                print 'It will take' ,round(years_to_save,2), 'years to save retirement funds'

# determine if number of years is even or odd
                num = int(years_to_save)
                if (num % 2) == 0:
                    print ' '
                    print 'If the number of years is ' ,num, ' then it is an even number'
                else:
                    print 'If the number of years is ' ,num, 'is an odd number'

