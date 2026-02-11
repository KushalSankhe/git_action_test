from main import add

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    from main import multiply
    assert multiply(2, 3) == 6