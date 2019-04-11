#FE 595A
#Midterm Assignment
#Team Members: Esther, Claude & Ken
#The initial code will be accepted to the project and we will modify as necessary


import re
import numpy as np
import glob
import nltk
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor



textcharacters = re.compile('[@_"!#$%^&*()<>?/\|}{~:;+]')

# Function checks if the string
# contains any special character
def run(string):
    while True:
        # Make own character set and pass
        # this as argument in compile method
        # Pass the string in search
        # method of regex object.
        if(textcharacters.search(string) == None):
            print("String is accepted")

        else:
            print("String is not accepted.")
        return




# Driver Code
if __name__ == '__main__' :

    # Enter the string
    string = name_input = input('Insert name: ')


    # calling run function
    run(string)



    blob = TextBlob(string)
    print (string)
    x = blob.sentiment
    #print("Polarity is: " + str(x))
    print(x)






