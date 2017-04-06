from __future__ import print_function
import requests
import numpy as np
import itertools
import time
import datetime

def calculate_lottery_date(date=datetime.datetime.today()):
    """Given a datetime parameter, the function will calculate the next irish
    lottery drawing. The Irish lottery draw takes place twice weekly on a
    Wednesday and a Saturday at 8pm. Write a function that calculates and returns the
    next valid draw date based on the current date and time and also on an optional supplied date.
    """
    future_date = None

    lottery_hour = 20
    saturday_weekday = 6
    wednesday_weekday = 3
    lottery_weekdays = set({wednesday_weekday, saturday_weekday})

    if date.isoweekday() in lottery_weekdays and date.hour == lottery_hour:
        future_date = date
    elif (date.isoweekday() >= wednesday_weekday and date.isoweekday() < saturday_weekday) or (date.hour > lottery_hour and date.hour < lottery_hour):
        print("We go Saturdays")
        days = abs(saturday_weekday - date.isoweekday())
    else:
        print("We go wednesday")
        days = abs(wednesday_weekday - date.isoweekday())
    print(days)
    hours_to_lottery = lottery_hour - date.hour
    if hours_to_lottery < 0:
        hours_to_lottery = 24 + hours_to_lottery
        days = days - 1
        print("Days {}".format(days))
    print(hours_to_lottery)
    minutes_to_lottery = (60 - date.minute) - 60
    print(minutes_to_lottery)
    seconds_to_lottery = (60 - date.second) - 60
    print(seconds_to_lottery)
    future_date = date + datetime.timedelta(days=days, hours=hours_to_lottery, minutes=minutes_to_lottery, seconds=seconds_to_lottery)

    return future_date.strftime("%d-%m-%Y %H:%M:%S")


def lru_cache(func, max_size = 100, caching_dict={}):
    def check_cache(*args):
        result = -1
        key = func.__name__
        timestamp = time.time()
        sorted_args = tuple(sorted(args))
        if key in caching_dict:
            if sorted_args in caching_dict[key]:
                result = caching_dict[key][sorted_args]['result']
                # Update timestamp
                caching_dict[key][sorted_args]['timestamp'] = timestamp
            else:
                if len(caching_dict[key]) == 0:
                    caching_dict[key] = {}

                caching_dict[key][sorted_args] = {'result': func(*args), 'timestamp': timestamp }
        else:
            caching_dict[key] = {}
            caching_dict[key][sorted_args] = {'result': func(*args), 'timestamp': timestamp}

        if len(caching_dict[key]) > max_size:
            oldest_timestamp = min([value['timestamp'] for value in caching_dict[key].values()])
            oldest_key = (key for key,value in caching_dict[key].items() if value['timestamp'] == oldest_timestamp)
            caching_dict[key].pop(next(oldest_key))


        result = caching_dict[key][sorted_args]['result']
        return result
    return check_cache


def anagrams_in_list(word, list_of_words):
    """Given a word (str) and list of words (list or tuple, a list is returned
    with the valid anagrams of the word in the list of words

    Args:
        - word (str): The word that you want to test
        - list_of_words (list or tuple): The list of words that you want to test against

    Returns:
        - list: A list with the valid anagrams of the word within the list of words

    """
    assert type(word) == str, "Expected '{}' to be type str, not {}".format(word, type(word))
    assert type(list_of_words) in (tuple, list), "Expected '{}' to be tuple or list, not {}".format(list_of_words, type(list_of_words))
    intersection_words = []

    response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
    if response.status_code == 200:
        # Valid english words
        response_text = response.text
        # Organize the words into an array
        array_words = np.array(response_text.split("\n"))
        # Get valid permutations of the word parameter
        valid_permutations = np.array(["".join(permutation).lower() for permutation in itertools.permutations(word)])

        valid_words = np.intersect1d(array_words, valid_permutations)

        filtered_words = valid_words[np.where(valid_words != word)]
        if filtered_words.size != 0:
            intersection_words = np.intersect1d(filtered_words, np.array(list_of_words))
        else:
            raise Exception('{} is not a valid word'.format(word))

    return intersection_words.tolist()
