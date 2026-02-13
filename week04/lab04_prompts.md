# Lab 04 - AI Prompts and Recommendations

## Problem 1: Finding Common Items

### Prompt
"I am working in Python in VS Code and need to implement a function that finds common product IDs between two very large lists (list1 and list2). Since these lists are massive, I'm worried about performance. The order of the resulting list doesn't matter. What is the most efficient data structure to use for this intersection, and can you provide the implementation for the find_common_elements function below?"

### AI Recommendation
**Data Structure: Sets**

**Reasoning:**
For finding common elements between two large lists, **sets** are the optimal choice because:
- **Time Complexity**: Converting lists to sets is O(n+m), and the intersection operation is O(min(n,m)). Finding intersection using lists would be O(n*m).
- **Lookup Performance**: Sets use hash tables internally, providing O(1) average lookup time vs. O(n) for lists.
- **Built-in Operations**: Python sets have a built-in `intersection()` method or the `&` operator, making the code concise and efficient.
- **No ordering requirement**: Since the problem states order doesn't matter, we don't need to preserve sequence, which is perfect for sets.

**Implementation:**
```python
def find_common_elements(list1, list2):
    """Find the common elements between two lists using sets."""
    return list(set(list1) & set(list2))
```

This converts both lists to sets, performs the intersection operation (`&` operator), and converts the result back to a list. Time complexity: O(n+m).

---

## Problem 2: User Profile Lookup

### Prompt
"I have a Python application where I frequently need to look up a user's profile (name, age, email) using their unique username. Currently, the data is loaded as a list of dictionaries, but I need to optimize this for high-performance lookups. What data structure should I use to store these profiles to ensure $O(1)$ search time? Please show me how to convert the list and implement the following function:"

### AI Recommendation
**Data Structure: Dictionary (Hash Map)**

**Reasoning:**
For user profile lookups by username, a **dictionary** is the optimal choice because:
- **Time Complexity**: Dictionary lookups are O(1) on average, compared to O(n) for searching through a list of dictionaries.
- **Key-Value Mapping**: The username becomes the key, and the entire user profile (name, age, email) becomes the value. This is exactly what a dictionary is designed for.
- **Lookup Performance**: Python dictionaries use hash tables internally, providing constant-time access to any user by their username.
- **Easy Access**: Once structured as a dictionary, you can fetch a user profile directly with `profiles[username]`.

**Implementation:**
```python
def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data."""
    # Convert list of dicts to a dictionary keyed by username for O(1) lookup
    user_dict = {user['name']: user for user in users}
    return user_dict.get(name)
```

This creates a dictionary comprehension where each user's name is the key and the entire user dictionary is the value. The `.get()` method returns the profile if found, or `None` if not found. Time complexity: O(n) for initial conversion, O(1) for each lookup.

---

## Problem 3: Listing Even Numbers in Order

### Prompt
"I am processing sensor data in Python. I need to filter a list of integers to return only the even numbers. Crucially, I must maintain the exact original order of the readings. Given that Python lists are ordered, is a standard list comprehension the best approach here, or is there a more memory-efficient structure (like a generator) I should consider for very large datasets? Please provide the implementation for:"

### AI Recommendation
**Data Structure: List Comprehension**

**Reasoning:**
For filtering even numbers while maintaining order, a **list comprehension** is the optimal choice because:
- **Time Complexity**: O(n) - must check every element regardless of approach.
- **Space Consideration**: Since the function signature specifies return type `list of int`, a list comprehension is appropriate and Pythonic.
- **Memory vs. Performance Trade-off**: While generators use less memory (lazy evaluation), they're best suited for streaming data. Since we need to return a complete list anyway, there's no memory advantage.
- **Order Preservation**: List comprehensions naturally preserve the original order of elements by iterating sequentially.
- **Readability**: List comprehension is clear, concise, and the most Pythonic way to express this filtering operation.
- **Real-world Application**: For sensor data where the full dataset fits in memory, list comprehension is ideal. For truly massive datasets that don't fit in memory, generators would be considered, but that's not typical for this use case.

**Implementation:**
```python
def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list."""
    return [num for num in numbers if num % 2 == 0]
```

This list comprehension iterates through `numbers`, checks if each number is even (`num % 2 == 0`), and includes it in the result list only if the condition is true. Order is preserved naturally through sequential iteration.
