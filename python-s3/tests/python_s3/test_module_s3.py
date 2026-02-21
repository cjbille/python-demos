from python_s3.module_s3 import add

def test_add_positive_numbers():
    a = 10
    b = 5
    result = add(a, b)
    assert result == 15
