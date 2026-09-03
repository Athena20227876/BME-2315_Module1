# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
define N

define a and b (a is 0 and b is 1 to start the fibonacci sequence)

start a counter at 0

create a variable to hold the sum of the numbers and start it at 0

create a while loop that runs while the counter is less than N

add b to the sum variable of total and replace total with this new number

calculate the next number in the sequence by adding a and b together

replace a with the previous value of b and replace b with the new next number

increase the counter by 1

outside of the while loop, print the total sum after the loop runs
"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # make a counter to keep track of how many numbers are being summed so that it can stay below N
total = 0 # variable holding sum of the numbers

while count < N: # run loop while the count is less than N
    total = total + b # add fibonacci number (b) to the total sum of the numbers

    next_value = a + b # to find next fibonacci number, add the previous two numbers together
    a = b # replace a with the previous b value
    b = next_value # replace b with the new next fibonacci number

    count = count + 1 # increase counter

print(total) # print the total sum of the first N fibonacci numbers after the loop concludes

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

def standard_deviation_fibonacci(N): # function that takes standard deviation of first N numbers in fibonacci sequence
    import numpy as np # import numpy library
    stnd_dev = np.std([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]) # calculate standard deviation of first N fibonacci numbers
    return stnd_dev # return standard deviation

print("The standard deviation of the first 10 numbers in the fibonacci sequence is: ", standard_deviation_fibonacci(10)) # print the standard deviation of the first 10 fibonacci numbers

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def fibonacci_sum(N): # function that takes the sum of N numbers in the fibonacci sequence
    a, b = 0, 1 #starting values for the fibonacci sequence
    total = 0 # variable to hold the sum of the numbers
    
    for _ in range(N):
        total += a # add current fibonacci number to the total sum
        a, b = b, a + b # update a and b to the next numbers in the fibonacci sequence
    
    return total # return the sum of the first N fibonacci numbers

N_values = [5, 10, 15, 20, 25, 30] # values of N given to calculate the sum

sums = [fibonacci_sum(N) for N in N_values] # list to hold sums of the first N fibonacci numbers

print(sums) # prints the list of sums

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0
    b = 1
    index = 0

    while a <= limit:
        next_value = a + b
        a = b
        b = next_value
        index += 1

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:  # This line checks if the Fibonacci number is even
            total += b
        a, b = b, a + b
    return total

print("The sum of all odd Fibonacci numbers less than 50 is: ", sum_even_fib(50))
# Add your test cases here

# %%
