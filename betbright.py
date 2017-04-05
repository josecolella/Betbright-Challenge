import requests
import numpy as np
import itertools


import datetime

def calculateLotteryDate(date=datetime.datetime.today()):
    lottery_hour = 8
    saturday_weekday = 5
    wednesday_weekday = 2
    lottery_weekdays = set(wednesday_weekday, saturday_weekday)

    if date.weekday() in lottery_weekdays and date.hour == lottery_hour:
        pass # Its the lottery
    if date.weekday >




# Test when the word is not valid
# Test when list of words are not valid


def foo(word, listOfWords):

    intersection_words = []

    response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
    if response.status_code == 200:
        response_text = response.text

        array_words = np.array(response_text.split("\n"))
        valid_permutations = np.array(["".join(permutation).lower() for permutation in itertools.permutations(word)])


        valid_words = np.intersect1d(array_words, valid_permutations)

        filtered_words = valid_words[np.where(valid_words != word)]
        if filtered_words.size != 0:
            intersection_words = np.intersect1d(filtered_words, np.array(listOfWords))
        else:
            pass # Not a valid word

    return intersection_words.tolist()





