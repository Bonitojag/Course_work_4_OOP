from abc import ABC, abstractmethod
import requests

class JobAPI(ABC):
    """
    Абстрактный класс для работы с API вакансий.
    Определяет методы get_vacancies и _send_request, которые должны быть реализованы в подклассах.
    """
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass

    @abstractmethod
    def _send_request(self, url: str, params: dict):
        pass


class HeadHunterAPI(JobAPI):
    """
    Класс для работы с API hh.ru.
    Реализует методы get_vacancies и _send_request для получения вакансий с hh.ru.
    """
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_query: str):
        params = {'text': search_query, 'area': '1'}
        response_data = self._send_request(self.__url, params)
        vacancies = response_data.get('items', [])
        return vacancies

    def _send_request(self, url: str, params: dict):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()






