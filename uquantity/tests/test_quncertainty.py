from astropy import units as u
from uquantity import UQuantity
import math


def test_simple_uquantity():
    ###
    a = UQuantity(5, u.km, 2)
    ##
    assert a.value == 5
    assert a.unit == u.km
    assert a.uncertainty == 2

def test_addition_uquantity():
    ###
    a = UQuantity(5, u.km, 2)
    b = UQuantity(12, u.km, 5)
    c = a + b
    ##
    assert c.value == 17
    assert c.unit == u.km
    # Uncertainties under addition add in quadrature
    assert c.uncertainty == math.sqrt(2**2 + 5**2)

def test_subtraction_uquantity():
    ###
    a = UQuantity(5, u.km, 2)
    b = UQuantity(12, u.km, 5)
    c = b - a
    ##
    assert c.value == 7
    assert c.unit == u.km
    # Uncertainties under subtraction add in quadrature
    assert c.uncertainty == math.sqrt(2**2 + 5**2)
