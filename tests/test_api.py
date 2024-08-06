import pytest
from unittest.mock import Mock
import requests
from src.api import HeadHunterAPI

@pytest.fixture
def api():
    return HeadHunterAPI()

def test_get_vacancies(api, mocker):
    # Подготовка mock-ответа
    mock_response = Mock()
    expected_data = {
        'items': [
            {'name': 'Повар', 'alternate_url': 'https://hh.ru/vacancy/104440635', 'salary': '60000-75000', 'snippet':  {'requirement': 'Опыт работы или профильное образование'}},
            {'name': 'Сварщик на полуавтомат', 'alternate_url': 'https://hh.ru/vacancy/105268866', 'salary': '70000', 'snippet': {'requirement': ' Полуaвтoматичeскaя сваpка узлов металлокoнcтрукций, подготовка деталей и узлов под сварочные швы.'}}
        ]
    }
    mock_response.json.return_value = expected_data
    mock_response.status_code = 200

    # Подмена requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Вызов метода
    vacancies = api.get_vacancies('Python')

    # Проверка
    assert len(vacancies) == 2
    assert vacancies[0]['name'] == 'Повар'
    assert vacancies[1]['name'] == 'Сварщик на полуавтомат'

def test_send_request_success(api, mocker):
    # Подготовка mock-ответа
    mock_response = Mock()
    expected_data = {'key': 'value'}
    mock_response.json.return_value = expected_data
    mock_response.status_code = 200

    # Подмена requests.get
    mocker.patch('requests.get', return_value=mock_response)

    # Вызов метода
    url = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python', 'area': '1'}
    response_data = api._send_request(url, params)

    # Проверка
    assert response_data == expected_data

def test_send_request_failure(api, mocker):
    # Подготовка mock-ответа с ошибкой
    mock_response = Mock()
    mock_response.status_code = 404

    # Подмена requests.get
    mocker.patch('requests.get', return_value=mock_response)
    mocker.patch('requests.get', side_effect=requests.exceptions.HTTPError)

    # Вызов метода и проверка исключения
    url = 'https://api.hh.ru/vacancies'
    params = {'text': 'Python', 'area': '1'}

    with pytest.raises(requests.exceptions.HTTPError):
        api._send_request(url, params)
