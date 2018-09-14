#ASTROWORLD - Rubin P., Puneet J., Ryan A.
#K06 - Divine Your Destiny!
#Period 7
#2018-09-13

from random import randint, choices

def parse_data(filename):
    file = open(filename, 'r')  #open the file in read mode
    raw = file.read()           #get the text
    list = raw.split("\n")      #split on new lines

    counter = 0
    while counter < len(list):  #loop thru it, splitting it on commas
        #remove unecessary quotes
        if '"' in list[counter]:        
            list[counter] = list[counter].replace('"', '')

        #splits on the last instance of a comma, once
        list[counter] = list[counter].rsplit(',', 1)
        counter += 1
    
    dict = {}
    counter = 1
    while counter < len(list) - 1:
        dict[list[counter][0]] = float(list[counter][1])
        counter += 1
    print(dict)
    return dict

def pick_job(dict):
    return
parse_data('occupations.csv')
