# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation
# of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_plates.py

from plates import is_valid

def test_plates():
    assert is_valid("C") == False
    assert is_valid("12") == False
    assert is_valid("CS50000") == False
    assert is_valid("12CS50") == False
    assert is_valid("CS./50") == False
    assert is_valid("CS50CS") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

