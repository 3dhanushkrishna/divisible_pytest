import Divisible
import pytest
@pytest.fixture
def input():
    x=25
    return x
def test_divisible5(input):

    result=Divisible.divisible_5(input)
    assert result==True
def test_divisible7(input):

    result=Divisible.divisible_7(input)
    assert result==False
def test_divisible9(input):

    result=Divisible.divisible_9(input)
    assert result==False
def test_divisible10(input):

    result=Divisible.divisible_10(input)
    assert result==False
