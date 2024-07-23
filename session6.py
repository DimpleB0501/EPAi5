import inspect
from numbers import Number

def check_docstring (fn):
    """This function is used to check if the function has a docstring with minimum 50 characters"""
    min_count = 50

    def count_docstring () -> bool:
        """
        if docstring > 50 characters, return True
        else return False
        """
        nonlocal min_count
        func_docstring = fn.__doc__
        if len(func_docstring) >  min_count:
            return True
        else:
            return False
    return count_docstring


def next_fibonacci_number():
    """
    Function to generate the next fibonacci number
    """
    num1 = 1
    num2 = 1

    def generate_number(num) -> int:
        """
        input: number after which you want to generate the fibonacci number
        output: generate fibonacci number greater than or equal to the given number
        """
        nonlocal num1, num2
        next_num = num1 + num2

        while next_num < num:
            #print ("Here---", next_num)
            num1 = num2
            num2 = next_num
            next_num = num1 + num2
        return next_num
    return generate_number


# Basic functions: add/mul/div functions
def add (num1: Number, num2: Number) -> Number:
    """
    Function to add 2 numbers
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
        raise TypeError("Only integer or float type arguments are allowed")



def mul (num1: Number, num2: Number) -> Number:
    """
    Function to multiply 2 numbers
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 * num2
    else:
        raise TypeError("Only integer or float type arguments are allowed")


def div (numerator: Number, denominator: Number) -> Number:
    """
    Function to divide 2 numbers
    """
    if isinstance(numerator, (int, float)) and isinstance(denominator, (int, float)):
        if denominator == 0:
            raise ValueError ("Divide by zero error")
        else:
            return numerator * denominator
    else:
        raise TypeError("Only integer or float type arguments are allowed")


# Closure function to count how many times a function is called and and update a global dictionary variable with the counts
dict_count = {'add': 0, 'mul': 0, 'div':0}

def func_counter_global_dict(fn):
    """
    Function to calculate the number of times a function is called.
    input: function
    ouput: global dictionary variable with the updated counts
    """
    count = dict_count[fn.__name__]
    def func_counter (*args, **kwargs):
        """
        Function updates the respective dictionary counter
        """
        fn(*args) # to raise type and value errors
        nonlocal count
        count += 1
        dict_count[fn.__name__] = count
        return count
    return func_counter


# Modify above such that now we can pass in different dictionary variables to update different dictionaries
def func_counter_variable_dict(fn, dict_counter:dict):
    """
    In this function we need to calculate the number of times a function is called and update the dictonary supplied by the user
    input: function, dictionary
    output: passed dictionary variable with the updated counts
    """
    count = dict_counter[fn.__name__]
    def func_counter_var(*args, **kwargs):
        """
        Function updates the respective dictionary counter
        """
        fn(*args) # to raise type and value errors
        nonlocal count
        count += 1
        dict_counter[fn.__name__] = count
        return count
    return func_counter_var
