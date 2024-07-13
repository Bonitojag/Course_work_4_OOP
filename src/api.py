from abc import ABC, abstractmethod
import requests

class JobAPI(ABC):
    """
    Абстрактный класс для работы с API вакансий.
    Определяет метод get_vacancies, который должен быть реализован в подклассах.
    """
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass

class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru.
    Реализует метод get_vacancies для получения вакансий с hh.ru.
    """
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str):
        params = {'text': search_query, 'area': '1'}
        response = requests.get(self.url, params=params)
        return response.json()

