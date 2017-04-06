import unittest
import datetime
from betbright import *

class TestCalculateLotteryDate(unittest.TestCase):

    def test_tuesday_date(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 11, 6, 0, 0))
        self.assertEqual('12-04-2017 20:00:00', date)

    def test_tuesday_after_hour(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 4, 21, 0))
        self.assertEqual('05-04-2017 20:00:00', date)

    def test_wednesday_after_hours(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 5, 21, 0))
        self.assertEqual('08-04-2017 20:00:00', date)

    def test_saturday_lottery(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 8, 20, 0))
        self.assertEqual('08-04-2017 20:00:00', date)

    def test_sunday_returns_next_wednesday(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 9, 6, 0))
        self.assertEqual('12-04-2017 20:00:00', date)

    def test_wednesday_on_lottery_day(self):
        date = calculate_lottery_date(datetime.datetime(2017, 4, 12, 20, 0))
        self.assertEqual('12-04-2017 20:00:00', date)


class TestLRUCache(unittest.TestCase):

    def test_add_cache(self):
        @lru_cache
        def add(x,y):
            return x+y

        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(2,3), 5)

    def test_substract_cache(self):
        @lru_cache
        def substract(x,y):
            return x-y

        self.assertEqual(substract(2,3), -1)
        self.assertEqual(substract(2,3), -1)
        self.assertEqual(substract(3,2), -1)
        self.assertEqual(substract(2,5), -3)


class TestAnagrams(unittest.TestCase):


    def test_arc_anagram(self):
         self.assertEqual(anagrams_in_list('car', ['arc', 'rac']), ['arc'])

	  
 

    def test_red_anagram(self):
        self.assertEqual(anagrams_in_list('red', ['der', 'rde']), ['der'])



if __name__ == '__main__':
    unittest.main(verbosity=2)
