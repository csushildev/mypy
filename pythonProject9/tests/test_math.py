import pytest
def add_two_numbers(a,b):
    return a+b

## when run pytest, file and function which start with test or tests is considered.
@pytest.mark.math
def test_small_number():
    assert add_two_numbers(1,2) == 3, "The sum of 1 and 2 should be 3"
@pytest.mark.math
def test_large_number():
    assert add_two_numbers(100, 200) == 300, "The sum of 100 and 200 should be 300"
