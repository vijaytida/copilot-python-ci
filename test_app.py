#use pytest to test the functions in app.py
from app import add
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(-1,-1) == -2

def test_subtract():
    from app import subtract
    assert subtract(5,2) == 3
    assert subtract(1,-1) == 2
    assert subtract(0,0) == 0
    assert subtract(-1,-1) == 0

def test_multiply():
    from app import multiply
    assert multiply(2,3) == 6
    assert multiply(-1,1) == -1
    assert multiply(0,0) == 0
    assert multiply(-1,-1) == 1
# add main function to run the tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print("All tests passed!")
