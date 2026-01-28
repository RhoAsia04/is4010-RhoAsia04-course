# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> You are a senior Python developer. I have a function that's supposed to sum all even numbers in a list, but it's giving wrong results. Here's the code:
> 
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>     
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>     
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
> 
> The function returns the wrong results. Can you identify the logical error in the conditional statement and provide the corrected version in a Python code block? Please explain what the bug was.

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.
    
    Parameters
    ----------
    numbers : list of int
        A list of integers.
    
    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: Changed from == 1 to == 0
            total += num
    return total
```

**What I Learned:**
The bug was a logical error in the condition. The original code checked `if num % 2 == 1`, which means "if the remainder when dividing by 2 is 1" (i.e., odd numbers). It should have been `if num % 2 == 0` to check for even numbers. A good practice is to test code with examples to catch these kinds of mistakes early.

---

## Problem 2: Refactoring

**My Prompt:**
> You are a senior Python developer who specializes in writing Pythonic code. I have a function that works correctly, but it's written in a confusing, non-Pythonic way. Here's the code:
> 
> ```python
> def get_names_of_adults(users):
>     """Given a list of user dictionaries, returns a list of names of users
>     who are 18 or older.
>     
>     Parameters
>     ----------
>     users : list of dict
>         List of user dictionaries with 'name' and 'age' keys.
>     
>     Returns
>     -------
>     list of str
>         Names of users who are 18 or older.
>     """
>     results = []
>     for i in range(len(users)):
>         if users[i]['age'] >= 18:
>             results.append(users[i]['name'])
>     return results
> ```
> 
> Can you refactor this to be more Pythonic? Focus on improvements like list comprehensions, better iteration patterns, and clearer variable names. Please provide the refactored code in a Python code block.

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.
    
    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.
    
    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user['name'] for user in users if user['age'] >= 18]
```

**What I Learned:**
The refactored version uses a list comprehension, which is more Pythonic and readable. Instead of manually indexing with `range(len(users))`, we iterate directly over the list with `for user in users`. The condition is also more intuitive when placed inside the comprehension. The refactored version is more concise (1 line vs 5 lines) while remaining clear and maintainable.

---

## Problem 3: Documenting

**My Prompt:**
> You are a senior Python developer who specializes in writing clear, professional documentation. I have a function that works correctly but has no documentation. Here's the code:
> 
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```
> 
> Can you write a professional NumPy-style docstring for this function? Include sections for Parameters, Returns, and Raises. Make sure to document that the function raises a ValueError for invalid inputs.

**AI's Corrected Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.
    
    Computes the area by multiplying the length and width of a rectangle.
    Both dimensions must be positive numbers.
    
    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.
    
    Returns
    -------
    float or int
        The area of the rectangle (length × width).
    
    Raises
    ------
    ValueError
        If length or width is less than or equal to 0.
    
    Examples
    --------
    >>> calculate_area(5, 4)
    20
    >>> calculate_area(3.5, 2)
    7.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**
NumPy-style docstrings are comprehensive and follow a consistent structure. The `Raises` section is important for documenting exceptions that functions can throw, which helps users understand error conditions. The `Examples` section with doctest-style examples is helpful for both documentation and testing. Good documentation makes code more maintainable and easier for other developers (and future you!) to understand.
