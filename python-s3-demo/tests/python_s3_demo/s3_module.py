from python_s3_demo.s3_module import add

def test_add_positive_numbers():
    a = 10
    b = 5
    result = add(a, b)
    assert result == 15
