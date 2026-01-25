#!/usr/bin/env python
"""Test script for lab02 functions."""

from week02.lab02 import factorial, is_prime, reverse_string

print("Testing factorial:")
print(f"  factorial(5) = {factorial(5)} (expected: 120)")
print(f"  factorial(0) = {factorial(0)} (expected: 1)")
print(f"  factorial(1) = {factorial(1)} (expected: 1)")
print()

print("Testing is_prime:")
print(f"  is_prime(17) = {is_prime(17)} (expected: True)")
print(f"  is_prime(4) = {is_prime(4)} (expected: False)")
print(f"  is_prime(1) = {is_prime(1)} (expected: False)")
print(f"  is_prime(2) = {is_prime(2)} (expected: True)")
print()

print("Testing reverse_string:")
print(f"  reverse_string('hello') = '{reverse_string('hello')}' (expected: 'olleh')")
print(f"  reverse_string('Python') = '{reverse_string('Python')}' (expected: 'nohtyP')")
print()

print("All tests completed!")
