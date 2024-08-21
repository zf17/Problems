# Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations
# of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
#  pytest test_fuel.py

from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("2.5/2")
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


