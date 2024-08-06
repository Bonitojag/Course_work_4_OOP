from abc import ABC, abstractmethod
import os
import json
from .vacancy import Vacancy

class VacancyStorage(ABC):
    """
    Абстрактный класс для работы с хранилищем вакансий.
    Определяет методы для добавления, получения и удаления вакансий.
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JSONSaver(VacancyStorage):
    """
    Класс для сохранения вакансий в JSON-файл.
    Реализует методы для добавления, получения и удаления вакансий.
    """
    def __init__(self, filename: str = 'vacancies.json'):
        self._filename = os.path.join('data', filename)
        os.makedirs('data', exist_ok=True)

    def add_vacancy(self, vacancy):
        data = self._load_data()
        if not any(vac['title'] == vacancy.title and vac['url'] == vacancy.url for vac in data):
            data.append(vacancy.__dict__)
        self._save_data(data)

    def get_vacancies(self, criteria: dict):
        data = self._load_data()
        filtered_vacancies = [Vacancy(**item) for item in data
                              if criteria['title'].lower() in item['title'].lower()
                              and self._salary_in_range(item.get('salary'), criteria['salary_from'], criteria['salary_to'])]
        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        data = self._load_data()
        data = [item for item in data if item['title'] != vacancy.title or item['url'] != vacancy.url]
        self._save_data(data)

    def _load_data(self):
        try:
            with open(self._filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self, data):
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def _salary_in_range(self, salary, salary_from, salary_to):
        if salary is None:
            return False
        return (salary.get('from') or 0) >= salary_from and (salary.get('to') or float('inf')) <= salary_to


