#FE 595A
#Midterm Assignment
#Team Members: Esther, Claude & Ken
#The initial code will be accepted to the project and we will modify as necessary



import re
import numpy as np
import glob
import nltk
from textblob import TextBlob, Word
from textblob.np_extractors import ConllExtractor
from textblob.classifiers import NaiveBayesClassifier



textcharacters = re.compile('[@_"!#$%^&*()<>?/\|}{~:;+]')

# Function checks if the string
# contains any special character
def run(string):
    while True:
        # Make own character set and pass
        # this as argument in compile method
        # Pass the string in search
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

    bbb = len(string.split())

    blob = TextBlob(string)
    x = blob.sentiment



    if bbb < 1100:

        #print (string)

        #print("Polarity is: " + str(x))
        #print(x)
        userchoiceless7 = input('Type in response of process you would like to observe: ')

        if (userchoiceless7 == 'tags'):
            print('tags')
            print(blob.tags)
            pluralizeinput = input('Would you like to pluralize Nouns?')
        elif (userchoiceless7 == 'noun phrases'):
            print('noun phrases')
            print (blob.noun_phrases)
        elif (userchoiceless7 == 'ngrams'):
            print(blob.ngrams(2))
        elif (userchoiceless7 == 'sentences'):
            #sentenceinput = input('Type in response of process you would like to observe: ')
            print('Total number of words in text entered is : '+ str(len(blob.words)))
            print('Total number of sentences in text entered is : '+ str(len(blob.sentences)))
            indexnumber = int(input('Which sentence would you like to view?, Enter index number here: '))
            print ('The text below corresponds to sentence # ' + str(indexnumber) + ':')
            print(blob.sentences[indexnumber-1])
            wordcountinput = input('Would you like to count the number of words in sentence #' +str(indexnumber) + ' ? ')
            if (wordcountinput) == 'yes':
                print (len(blob.sentences[indexnumber-1].words))
                inflectioninput= input('Would you like to display Word Inflection? ')
                if inflectioninput == 'yes':
                    inflectioninput2 = int(input('Enter any number index for the word you would like to singularize '))
                    print(blob.sentences[indexnumber-1].words[inflectioninput2].singularize())
                else:
                    print('Thank you')
            else:
                print ('Thank you.')
        elif (userchoiceless7 == 'translate'):
            print ('translate')
            translate_response = input('Choose 1 translation option from the following list of languages: English, Arabic, Chinese, Spanish, Thai, Russian, Portuguese, Japenese, Greek, German, French, Dutch ')
            if (translate_response == 'english'):
                print(blob.translate(to='en'))
            elif (translate_response =='arabic'):
                print(blob.translate(to='ar'))
            elif (translate_response =='chinese'):
                print(blob.translate(to='zh'))
            elif (translate_response =='spanish'):
                print(blob.translate(to='es'))
            elif (translate_response =='thai'):
                print(blob.translate(to='th'))
            elif (translate_response =='russian'):
                print(blob.translate(to='ru'))
            elif (translate_response =='portuguese'):
                print(blob.translate(to='pt'))
            elif (translate_response =='japenese'):
                print(blob.translate(to='ja'))
            elif (translate_response =='greek'):
                print(blob.translate(to='el'))
            elif (translate_response =='german'):
                print(blob.translate(to='de'))
            elif (translate_response =='french'):
                print(blob.translate(to='fr'))
            elif (translate_response =='dutch'):
                print(blob.translate(to='nl'))
            else:
                print ('next lange')
        else:
        #print(bbb)
            blob = TextBlob(string)
            print('kjkjjk') # do something different here


else:
    print('the end')






