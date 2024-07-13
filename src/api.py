from abc import ABC, abstractmethod
import requests

class JobAPI(ABC):
    """
    ����������� ����� ��� ������ � API ��������.
    ���������� ����� get_vacancies, ������� ������ ���� ���������� � ����������.
    """
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass

class HeadHunterAPI(JobAPI):
    """
    ����� ��� ������ � API hh.ru.
    ��������� ����� get_vacancies ��� ��������� �������� � hh.ru.
    """
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str):
        params = {'text': search_query, 'area': '1'}
        response = requests.get(self.url, params=params)
        return response.json()

