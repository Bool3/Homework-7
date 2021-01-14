# Advanced Topics in Computer Science
## Homework 8 (20 pts)
### Due: January 20, 2021
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


## Euclidian Similarity Score

Write a function ```sim_euclidean``` that returns a similarity score between students based on their euclidean distance.

Your function should pass the following assertions: 

```
assert math.isclose( sim_euclidean(test_db,'student914','student9804'), 0.0384, rel_tol = 0.009 )
assert math.isclose( sim_euclidean(test_db,'student5231','student4157'), 0.1, rel_tol = 0.009 ) 
assert math.isclose( sim_euclidean(test_db,'student1397','student7408'), 0.05, rel_tol = 0.009 )

```

## Pearson Correlation Coefficients

Write a function, ```sim_pearson```, that returns the pearson correlation coefficient between 2 students.

Your function should pass the following assertions:

```  

assert math.isclose( sim_pearson(test_db,'student914','student9804'), 0.63246
, rel_tol = 0.0009 )
assert math.isclose( sim_pearson(test_db,'student5231','student4157'), -0.48038, rel_tol = 0.0009 ) 
assert math.isclose( sim_pearson(test_db,'student1397','student7408'), -0.23338, rel_tol = 0.0009 )

```

## Your Closest Classmates

Write a function, ``` top_matches(db, student, n=5, simFn = sim_euclidean) ``` that returns a list with the top ``` n ``` ```(student_id, score)``` pairs for ```student```. The ```simFn``` parameter will let you specify which similarity score to use in the comparison.

Once you have completed the first sections above, report your results to me. I will then tell you your ```studentID```. Find the studentId's, sorted by similarity that you are most similar to using both similarity scores. 


