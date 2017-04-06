# Betbright-Challenge

Exercises for the Betbright challenge.


## Exercises 1

For this exercise, I utilized datetime and timedelta to calculate the next lottery draw. I utilized a mapping that would provide the difference between the days of the weeks and the days that the lottery is drawn. Then using timedelta calculate the future date. 


## Exercises 2

For this exercise, I utilized the dictionary as the cache. Basically the function names become the 1st level keys, then each time the method is called, the parameters that are passed become the inner key with the result put in the result key and a timestamp that is used for keeping track of the least recently used item in the dictionary. Once the `max_size` is reached, the arguments are popped.

So the structure of the cache is the following:

```python
@lru_cache
def add(x,y):
  return x + y
  
 add(2,3)
 # Cache = {'add': {(2,3): 5}}
 add(3,4)
 # Cache = {'add': {(2,3): 5, (3,4): 7}}
```


## Exercises 3

For this third exercise, I utilized the `itertools.permutations` module method to provide the different combinations of the word that is passed as a parameters. All valid words are fetched, and the word parameter and list of words parameters are checked to see if they are valid words. Numpy arrays are used to hold the data. This was chosen for scalability, as it can manage large-sums of data in an efficient manner



## Requirements

- numpy

##LICENSE MIT

Copyright (c) 2017 Jose.Colella

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
