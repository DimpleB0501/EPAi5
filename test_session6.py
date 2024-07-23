import pytest
import random
import string
import session6
import os
import inspect
import re
import math
import time

README_CONTENT_CHECK_FOR = [
    'closure',
    'docstring',
    'fibonacci',
    'counter',
    'dictionary',
    'global'
]

def test_session6_readme_exists():
    """ A. failure_message: Found README.md file
        B. Once you write this test, it needs to print the filures_message for failing this test.
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    """ A. failures_message: Make your README.md file interesting! Add atleast 500 words
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    readme_word = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_word) >= 10, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_session6_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
        A.  failures_message_1: Your script contains misplaced indentations
            failures_message_2: Your code indentation does not follow PEP8 guidelines
        B. Once you write this test, it needs to print the failures_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"



def test_session6_function_name_had_cap_letter():
    """ A. failures_message: You have used Capital letter(s) in your function names
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

# Test 1: Docstring present or not
def test_session6_docstring ():
    """Tests to validate the presence of doc string
    """
    assert bool(session6.check_docstring.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.next_fibonacci_number.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.add.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.mul.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.div.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.func_counter_global_dict.__doc__) == True, "Docstring missing or less than 50 characters"
    assert bool(session6.func_counter_variable_dict.__doc__) == True, "Docstring missing or less than 50 characters"

# Test 2: Functions written as closures
def test_session6_closure():
    fn = session6.check_docstring(session6.next_fibonacci_number)

    assert bool(fn.__closure__) == True, "Closure not written"
    fn = session6.next_fibonacci_number()

    assert bool(fn.__closure__) == True, "Closure not written"

    func = session6.add
    fn = session6.func_counter_global_dict(func)
    assert bool(fn.__closure__) == True, "Closure not written"
    fn = session6.next_fibonacci_number()

    var_dict = {'add':0, 'mul':0}
    fn = session6.func_counter_variable_dict(func, var_dict)
    assert bool(fn.__closure__) == True, "Closure not written"

# Test 3: Check function is passed to docstring
def test_session6_function_passed_docstring():
    #fn = session6.check_docstring(session6.next_fibonacci_number)
    fn = session6.check_docstring(50)


# Test 4:


# Test 1: Closure based n-th fibonacci number
def test_nth_fibonacci():
    fibonacci = session6.next_fibonacci_number()
    assert (fibonacci(6)) == 8, "Fibonacci number not generated "

# Test 2: Closure based n-th fibonacci number
def test_nth_fibonacci():
    fibonacci = session6.next_fibonacci_number()
    #print (fibonacci(3))
    assert (fibonacci(3)) == 3, "Fibonacci number not generated "

# Test 1: counter with global dictonary

def test_mycounter_with_global_dict():
    mydict_val = {'add':4,'mul':3,'div':2}
    fn = session6.add
    value = session6.func_counter_global_dict(fn)
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    fn = session6.mul
    value = session6.func_counter_global_dict(fn)
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    fn = session6.div
    value = session6.func_counter_global_dict(fn)
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    assert session6.dict_count == mydict_val,'just count how many times each funtion is called..'

def test_mycounter_with_global_dict_v2():
    mydict_val = {'add':4,'mul':3}
    mypersonaldict= {'add':0,'mul':0}
    fn = session6.add
    value = session6.func_counter_variable_dict(fn,mypersonaldict)
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    fn = session6.mul
    value = session6.func_counter_variable_dict(fn,mypersonaldict)
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    value(random.randint(1,100),random.randint(1,100))
    assert mypersonaldict == mydict_val,'just count how many times each funtion is called..'
