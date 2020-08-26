import pandas as pd

name = ['Taylor Swift', 'Aaron Sorkin', 'Harry Potter', 'Ji-Sung Park']
birthday = ['December 13, 1989', 'June 9, 1961', 'July 31, 1980', 'February 25, 1981']
occupation = ['Singer-songwriter', 'Screenwriter', 'Wizard', 'Footballer']

dict1 = {
    'name': name,
    'birthday': birthday,
    'occupation': occupation
}

df = pd.DataFrame(dict1)

df
# --------------------------------------------------------------------------------------------------------------
#	  name	        birthday	        occupation
#0	Taylor Swift	December 13, 1989	Singer-songwriter
#1	Aaron Sorkin	June 9, 1961	    Screenwriter
#2	Harry Potter	July 31, 1980	    Wizard
#3	Ji-Sung Park	February 25, 1981	Footballer
