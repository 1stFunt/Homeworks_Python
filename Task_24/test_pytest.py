import pytest
from roots import find_roots

def test_valid_inputs():
    assert find_roots(1, -3, 2) == (2.0, 1.0)
    assert find_roots(1, 2, 1) == (-1.0, -1.0)
    assert find_roots(1, 1, 2) == ((-0.5+1.3228756555322954j), (-0.5-1.3228756555322954j))

def test_invalid_inputs():
    with pytest.raises(TypeError):
        find_roots("a", 2, 1)

def test_special_cases_1():
    with pytest.raises(ValueError, match="Уравнение имеет бесконечно много корней."):
        find_roots(0, 0, 0)

def test_special_cases_2():
    with pytest.raises(ValueError, match="Уравнение не имеет корней."):
        find_roots(0, 0, 1)

if __name__ == '__main__':
    pytest.main()