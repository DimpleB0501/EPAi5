# Instructions
- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200 <br/>
- Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100 ----- done <br/>
- We wrote a closure that counts how many times a function was called. Write a new one that can keep track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250 <br/>
- Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250 <br/>
- Once done, upload the code to Git Hub, run actions, and then proceed to answer S6 - Assignment Solutions. <br/>
No readme or no docstring for each function, or no test cases (4, 2, 6, 6, >7 = 25 tests), then 0. Write atleast 7 test cases to check boundary conditions that might cause your code to fail. Scores = Total Tests * 5 + Total Cleared Tests * 5


# Assignment
Written closures for the functions mentioned below
### check_docstring
```
Input - function
Output - True or False, based on whether the docstring of the passed function is present and greater than 50 characters
```
This function checks whether docstring is present for the passed function.

### next_fibonacci_number
```
Input - number
Output - generate fibonacci number greater than or equal to the given number
```
This function generates the next fibonacci number based on the given number.

### func_counter_global_dict
```
Input - function
Output - global dictionary displaying respective counters
```
Function to calculate the number of times a function is called.

### func_counter_variable_dict
```
Input - function, dictonary
Output - passed dictionary variable with the updated counts

```
In this function we calculate the number of times a function is called and update the dictonary supplied by the user.
