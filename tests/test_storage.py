import pytest
import os
import json
from src.storage import JSONSaver, Vacancy

@pytest.fixture
def sample_vacancy():
    return Vacancy(title="Back-end разработчик Python/Django", url="https://hh.ru/vacancy/105236858", salary={"from": 65000, "to": 70000})

@pytest.fixture
def json_saver():
    saver = JSONSaver(filename='test_vacancies.json')
    # Удалим тестовый файл перед каждым запуском тестов, чтобы начинать с чистого состояния
    if os.path.exists(saver._filename):
        os.remove(saver._filename)
    return saver

def test_add_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    data = json_saver._load_data()
    assert len(data) == 1
    assert data[0]['title'] == "Back-end разработчик Python/Django"

def test_get_vacancies(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    criteria = {"title": "Back-end разработчик Python/Django", "salary_from": 50000, "salary_to": 250000}
    vacancies = json_saver.get_vacancies(criteria)
    print("Vacancies:", vacancies)  # Debug: Печать вакансий
    assert len(vacancies) == 1
    assert vacancies[0].title == "Back-end разработчик Python/Django"

def test_delete_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    json_saver.delete_vacancy(sample_vacancy)
    data = json_saver._load_data()
    assert len(data) == 0


