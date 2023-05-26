import sys
sys.path.append('../')
from exercice1 import Calculator

def test_add():
    assert Calculator.add(Calculator, 1, 2) == 3

def test_subtract():
    assert Calculator.subtract(Calculator, 1, 2) == -1

def test_multiply():
    assert Calculator.multiply(Calculator, 1, 2) == 2

def test_divide():
    assert Calculator.divide(Calculator, 1, 2) == 0.5

def test_power():
    assert Calculator.power(Calculator, 1, 2) == 1

def test_sqrt():
    assert Calculator.sqrt(Calculator, 1) == 1
