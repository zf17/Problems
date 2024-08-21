from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hElLo") == "hlL"
    assert shorten("he11o") == "h11"
    assert shorten("he..o") == "h.."

# Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation 
# of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
