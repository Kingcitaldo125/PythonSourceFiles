import pytest

from ..binary_search import binary_search

def test_empty():
	xl = []
	assert binary_search(xl, 1) == False

def test_yes_front():
	xl = [1,2,3,4]
	assert binary_search(xl, 1) == True

def test_yes_back():
	xl = [1,2,3,4]
	assert binary_search(xl, 4) == True

def test_no_front():
	xl = [1,2,3,4]
	assert binary_search(xl, 0) == False

def test_no_back():
	xl = [1,2,3,4]
	assert binary_search(xl, 5) == False

def test_yes_range_positive():
	for i in range(1,100):
		assert binary_search([j for j in range(1,100)],i) == True

def test_yes_range_negative():
	for i in range(-100,101):
		assert binary_search([j for j in range(-100,101)],i) == True

def test_no_range():
	for i in range(100,1001):
		assert binary_search([j for j in range(1,100)],i) == False
