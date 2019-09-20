""" Basic test function """
def add_one(num_x):
    """ Adds 1 to function parameter """
    return num_x + 1


def test_answer():
    """ compares return value of add_one to a value """
    assert add_one(4) == 5
