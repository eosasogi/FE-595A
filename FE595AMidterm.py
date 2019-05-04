import random
from numpy import random
import sys
import re
import numpy as np
import glob
import nltk
from textblob import TextBlob, Word
from textblob.en.sentiments import NaiveBayesAnalyzer
from textblob.np_extractors import ConllExtractor
from textblob.classifiers import NaiveBayesClassifier


textcharacters = re.compile('[@_!#$%^&*()<>?/\|}{~;+]')

# Function checks if the string
# contains any special character
def run(string):
    while True:
        # Make own character set and pass
        # this as argument in compile method
        # Pass the string in search
        if(textcharacters.search(string) == None):
            print("Your input has been accepted.")
            print('The following options are available to process input text: Tags, Sentiment, Noun Phrases, Ngrams, Sentences and Translate')

        else:
            print("Your input has not been accepted.")
        return


# Driver Code
if __name__ == '__main__' :

    # Enter the string
    string = name_input = input('Paste or type text that you would like to analyze here: ')

    # calling run function
    run(string)

    bbb = len(string.split())

    blob = TextBlob(string, analyzer= NaiveBayesAnalyzer())
    x = blob.sentiment


    if bbb < 100:

        #print("Polarity is: " + str(x))

        userchoiceless7 = input('Type in response of process you would like to observe: ')

        if (userchoiceless7.lower() == 'tags'):
            print(blob.tags)
            print ("Thank you!")
        elif (userchoiceless7.lower() == 'sentiment'):
            if x[0] == 'pos':
                print('The sentiment of the input text is Positive')
                print ("Thank you!")

            else:
                print('The sentiment of the input text is Negative')
                print ("Thank you!")

        elif (userchoiceless7.lower() == 'noun phrases'):
            print (blob.noun_phrases)
            print ("Thank you!")
        elif (userchoiceless7.lower() == 'ngrams'):
            print(blob.ngrams(2))
            print ("Thank you!")
        elif (userchoiceless7.lower() == 'sentences'):
            #sentenceinput = input('Type in response of process you would like to observe: ')
            print('Total number of words in text entered is : '+ str(len(blob.words)))
            print('Total number of sentences in text entered is : '+ str(len(blob.sentences)))
            indexnumber = int(input('Which sentence would you like to view?, Enter index number here: '))
            print ('The text below corresponds to sentence # ' + str(indexnumber) + ':')
            if (indexnumber > 0):
                print(blob.sentences[indexnumber-1])
            else:
                print(blob.sentences[0])

            wordcountinput = input('Would you like to count the number of words in sentence #' +str(indexnumber) + ' ? ')
            if (wordcountinput.lower()) == 'yes':
                print (len(blob.sentences[indexnumber-1].words))
                inflectioninput= input('Would you like to display Word Inflection? ')
                if inflectioninput.lower() == 'yes':
                    inflectioninput2 = int(input('Enter any number index for the word you would like to singularize: '))
                    print(blob.sentences[indexnumber-1].words[inflectioninput2].singularize())
                    print ("Thank you!")
        elif (userchoiceless7.lower() == 'translate'):
            translate_response = input('Choose 1 translation option from the following list of languages: English, Arabic, Chinese, Spanish, Thai, Russian, Portuguese, Japenese, Greek, German, French, Dutch ')
            if (translate_response.lower() == 'english'):
                print(blob.translate(to='en'))
                print ("Thank you!")
            elif (translate_response.lower() =='arabic'):
                print(blob.translate(to='ar'))
                print ("Thank you!")
            elif (translate_response.lower() =='chinese'):
                print(blob.translate(to='zh'))
                print ("Thank you!")
            elif (translate_response.lower() =='spanish'):
                print(blob.translate(to='es'))
                print ("Thank you!")
            elif (translate_response.lower() =='thai'):
                print(blob.translate(to='th'))
                print ("Thank you!")
            elif (translate_response.lower() =='russian'):
                print(blob.translate(to='ru'))
                print ("Thank you!")
            elif (translate_response.lower() =='portuguese'):
                print(blob.translate(to='pt'))
                print ("Thank you!")
            elif (translate_response.lower() =='japenese'):
                print(blob.translate(to='ja'))
                print ("Thank you!")
            elif (translate_response.lower() =='greek'):
                print(blob.translate(to='el'))
                print ("Thank you!")
            elif (translate_response.lower() =='german'):
                print(blob.translate(to='de'))
                print ("Thank you!")
            elif (translate_response.lower() =='french'):
                print(blob.translate(to='fr'))
                print ("Thank you!")
            elif (translate_response.lower() =='dutch'):
                print(blob.translate(to='nl'))
                print ("Thank you!")

    else:

        nouns = list()

        for word, tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())

                print ("This text is about...")

                for item in random.choice(nouns, 5):
                    word = Word(item)
                    print (word.pluralize())
