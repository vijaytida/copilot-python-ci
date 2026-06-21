#use pytest to test the functions in app.py
from app import add
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(-1,-1) == -2

# add main function to run the tests
if __name__ == "__main__":
    test_add()
    print("All tests passed!")
    