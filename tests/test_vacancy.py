import pytest
from src.vacancy import Vacancy

@pytest.fixture
def sample_vacancy():
    return Vacancy('Разработчик (SQL Python)', 'https://hh.ru/vacancy/105296322', {'from': 50000, 'to': 70000, 'currency': 'RUB'}, '<highlighttext>Описание</highlighttext>')

def test_vacancy_init():
    with pytest.raises(ValueError):
        Vacancy(123, 'hhttps://hh.ru/vacancy/105296322', {'from': 50000}, 'Description')
    with pytest.raises(ValueError):
        Vacancy('Разработчик (SQL Python)', 123, {'from': 50000}, 'Description')
    with pytest.raises(ValueError):
        Vacancy('Разработчик (SQL Python)', 'https://hh.ru/vacancy/105296322', 'salary', 'Description')
    with pytest.raises(ValueError):
        Vacancy('Разработчик (SQL Python)', 'https://hh.ru/vacancy/105296322', {'from': 'not a number'}, 'Description')

def test_vacancy_str(sample_vacancy):
    expected_str = "Разработчик (SQL Python) - 50000 - 70000 RUB\nhttps://hh.ru/vacancy/105296322\nОписание"
    assert str(sample_vacancy) == expected_str

def test_vacancy_comparison(sample_vacancy):
    other_vacancy = Vacancy('Middle Data Scientist', 'https://hh.ru/vacancy/105038839', {'from': 110000, 'to': 250000, 'currency': 'RUB'})
    assert sample_vacancy < other_vacancy
    assert sample_vacancy <= other_vacancy
    assert not (sample_vacancy > other_vacancy)
    assert not (sample_vacancy >= other_vacancy)
    assert sample_vacancy != other_vacancy

def test_vacancy_clean_description(sample_vacancy):
    assert sample_vacancy.description == 'Описание'

def test_vacancy_get_salary(sample_vacancy):
    assert sample_vacancy.get_salary() == 50000

def test_vacancy_equality(sample_vacancy):
    same_vacancy = Vacancy('Разработчик (SQL Python)', 'https://hh.ru/vacancy/105296322', {'from': 50000, 'to': 70000, 'currency': 'RUB'}, 'Description')
    assert sample_vacancy == same_vacancy

