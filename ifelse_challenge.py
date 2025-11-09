def num_days(month):
    thirty_one = ("jan", "mar", "may", "jul", "aug", "oct", "dec" )
    thirty = ("apr", "jun", "sep", "nov")

    if month in thirty_one:
        print('number of days in',month,'is',31)
    elif month in thirty:
        print('number of days in',month,'is',30)
    else:
        print('number of days in',month,'is',28)

num_days('feb')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
