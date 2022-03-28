import Divisible
import pytest
def test_divisible5():
    x=5
    result=Divisible.divisible_5(x)
    assert result==True
def test_divisible7():
    x=14
    result=Divisible.divisible_7(x)
    assert result==True
def test_divisible9():
    x=27
    result=Divisible.divisible_9(x)
    assert result==True
def test_divisible10():
    x=50
    result=Divisible.divisible_10(x)
    assert result==True
