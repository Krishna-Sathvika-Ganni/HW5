'''Calculator Test'''
from app.calculator import Calculator

def test_addition():
    '''Test that addition function works '''  
    cal=Calculator()
    assert cal.add(5,2) == 7

def test_subtraction():
    '''Test that subtraction function works '''   
    cal=Calculator()
    assert cal.subtract(3,2) == 1

def test_multiplication():
    '''Test that Multiplication function works'''
    cal=Calculator()
    assert cal.multiply(3,4) == 12

def test_division():
    '''Test that Division function works'''
    cal=Calculator()
    assert cal.divide(10,5) == 2

#End