import pytest
from src.utils import parse_salary_range


def test_parse_salary_range():
    assert parse_salary_range("1000-2000") == (1000, 2000)
    assert parse_salary_range("3000") == (3000, float('inf'))
    assert parse_salary_range("") == (0, float('inf'))
    assert parse_salary_range(None) == (0, float('inf'))
    assert parse_salary_range("  1500 - 2500  ") == (1500, 2500)

    with pytest.raises(ValueError):
        parse_salary_range("abc-def")

    with pytest.raises(ValueError):
        parse_salary_range("1000-abc")
