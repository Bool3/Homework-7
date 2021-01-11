# Advanced Topics in Computer Science

## Homework 7 (20 pts)

### Due: January 15, 2021

#### SUBMISSION FILE: lastname\_hw7.py OR lastname\_hw7.ipynb OR lastname\_hw7.zip

__!! submit with the correct file name !!__

---

#### Note On Group Work

For this assignment you __may__ get assistance from your classmates. You __may not__ use resources online. If you have any questions or doubts defintely ask.

__DO NOT MAKE ANY ASSUMPTIONS ON WHAT IS OR IS NOT A VALID SOURCE!__. 

__ASK ME!__ 

---

## On Code Quality 

### Code Readability

The readability of your code __will__ matter this time. Make sure that you are using variable, class, function, and method names that are descriptive. Make sure that you are not being _too_ clever with your code, or that if you are you use comments to explain non-obvious statements and expressions. Use document strings to summarize the output of function and method calls. The purpose of this is __NOT__ busy work. The purpose of this is to make your code more readable for others, even if others is _Future You_.

### Testing

You are expected to use tests when developing your code. We have not covered this in class, but this is an excellent habit of professional coders. This does not have to be an onerous exercise. Simply using ```assert``` statements liberally will get you a lot of mileage.

### Logging

To help with your development and debugging consider using the Python ```logging``` module. Read here, [Python Logging](https://realpython.com/python-logging/) for a quick overview of how to use it. Below is an example usage.

```
import logging


def setup_logging(level=logging.DEBUG):
  logging.basicConfig(level=level, format='%(asctime)s{%(levelname)s} %(message)s',datefmt='%H:%M:%S')
  
  # shorthand convenience methods for using logger
  global debug, warn, info, error, crash
  
  debug = logging.debug
  warn = logging.warning
  info = logging.info
  error = logging.error
  crash = logging.critical

# initialize logger
# debug and warn messages will be skipped
setup_logging(logging.WARNING)

```
---

# Problem Set

## Build a Test Data Set

Make a test data set, ```test_db```, from the student database. Your data set should have:

* Advanced students only
* Ratings for the following songs only: ``` ["Kiss","Scrubs","Space Cowboy","Pollyana","Moonlight Sonata","Young Dumb and Broke","Feeling Good"]```

Your code should pass the following test:

```
ids = ['student1397', 'student1890', 'student4157', 'student4917', 'student5231', 'student632', 'student7408', 'student914', 'student9279', 'student9550', 'student9804']

assert len(test_db) == 11
assert all( id in ids for id in test_db.keys())

```

## Helper Function
Write a helper function that returns the songs that 2 students have each rated. 

**Write this function on your own first!!** When you have a function implemented then refer to [this article](https://www.geeksforgeeks.org/python-intersection-two-lists/) that shows several different ways to accomplish the same thing. 

Below is the output from my function. You should have the same output although your function may have a different signature.

```
shared('914','9804')

# returns the following 
['Space Cowboy', 'Feeling Good', 'Scrubs', 'Young Dumb and Broke', 'Kiss', 'Moonlight Sonata']

shared('student5231','student4157')

# returns the following 
['Scrubs', 'Pollyana', 'Young Dumb and Broke', 'Kiss', 'Moonlight Sonata']


shared('student1397','student7408')

# returns the following 
['Space Cowboy', 'Feeling Good', 'Scrubs', 'Pollyana', 'Young Dumb and Broke', 'Kiss', 'Moonlight Sonata']

```

## Euclidian Distance

Write a function, ```euclidean```, that implements euclidean distance between 2 students. Remember that the euclidian distance should only consider the songs that _both_ of the students have ranked. In other words use your function from the previous section in your implementation.

The signature for your function is as follows:

```
euclidean(dictionary_key_studentId_value_ratings, studentId_1, studentId_2)
```

Your code should pass the following assertions. Notice that I am using the ```isclose``` method to compare the floats:

```
assert math.isclose( euclidean(test_db,'student914','student9804'), 5.0 )
assert math.isclose( euclidean(test_db,'student5231','student4157'), 3.0 )
assert math.isclose( euclidean(test_db,'student1397','student7408'), 4.3589, rel_tol=0.0009 )

```

