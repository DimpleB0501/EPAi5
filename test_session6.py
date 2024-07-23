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

def test_session6_readme_100_words():
    """ A. failures_message: Make your README.md file interesting! Add atleast 100 words
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully.
    """
    readme_word = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_word) >= 100, "Make your README.md file interesting! Add atleast 100 words"


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

# Test 3: Closure based n-th fibonacci number
def test_nth_fibonacci():
    fibonacci = session6.next_fibonacci_number()
    assert (fibonacci(6)) == 8, "Fibonacci number not generated "

# Test 4: Closure based n-th fibonacci number
def test_nth_fibonacci():
    fibonacci = session6.next_fibonacci_number()
    #print (fibonacci(3))
    assert (fibonacci(3)) == 3, "Fibonacci number not generated "


# Test 5: function counter with global dictonary
def test_counter_with_global_dict():
    dict_check = {'add':2,'mul':3,'div':2}
    add_func = session6.func_counter_global_dict(session6.add)
    mul_func = session6.func_counter_global_dict(session6.mul)
    div_func = session6.func_counter_global_dict(session6.div)

    add_func(2, 3)
    add_func(6, 4)

    mul_func(2, 2)
    mul_func(2, 4)
    mul_func(2, 2)

    div_func(4, 2)
    div_func(10, 5)
    assert session6.dict_count == dict_check,'function counter is not working'

# Test 6: function counter with passed dictionary
def test_func_counter_variable_dict():
    dict_check = {'add':5,'mul':3}
    dict_func = {'add':0,'mul':0}

    add_func = session6.func_counter_variable_dict(session6.add, dict_func)
    mul_func = session6.func_counter_variable_dict(session6.mul, dict_func)

    add_func(1, 1)
    add_func(2, 10)
    add_func(3, 20)
    add_func(4, 30)
    add_func(5, 40)

    mul_func(2, 2)
    mul_func(3, 3)
    mul_func(5, 5)

    assert dict_func == dict_check,'function counter is not working'

# Test 7: function counter to check only int and float are passed in case of add, mul and div functions
def test_func_counter_correct_params():
    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed*"):
        add_fn = session6.func_counter_global_dict(session6.add)
        add_fn(2,'hello')

    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed*"):
        mul_fn = session6.func_counter_global_dict(session6.mul)
        mul_fn(2,'world')

    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed*"):
        div_fn = session6.func_counter_global_dict(session6.div)
        div_fn(2,'err')

# Test 8: function counter to check for divide by zero error in div funtion
def test_func_counter_divide_zero():
    with pytest.raises(ValueError, match=r".*Divide by zero error*"):
        div_fn = session6.func_counter_global_dict(session6.div)
        div_fn(2, 0)
