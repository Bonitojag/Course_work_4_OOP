import os
import json
from abc import ABC, abstractmethod
from .vacancy import Vacancy


class VacancyStorage(ABC):
    """
    Абстрактный класс для работы с хранилищем вакансий.
    Определяет методы для добавления, получения и удаления вакансий.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет вакансию в хранилище.
        """
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict):
        """
        Получает вакансии из хранилища по заданным критериям.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаляет вакансию из хранилища.
        """
        pass


class JSONSaver(VacancyStorage):
    """
    Класс для сохранения вакансий в JSON-файл.
    Реализует методы для добавления, получения и удаления вакансий.
    """

    def __init__(self, filename: str):
        """
        Инициализирует JSONSaver с заданным именем файла.
        """
        self.filename = os.path.join('data', filename)
        os.makedirs('data', exist_ok=True)

    def add_vacancy(self, vacancy: Vacancy):
        """
        Добавляет вакансию в JSON-файл.
        """
        data = self._load_data()
        data.append(vacancy.__dict__)
        self._save_data(data)

    def get_vacancies(self, criteria: dict):
        """
        Получает вакансии из JSON-файла по заданным критериям.
        """
        data = self._load_data()
        filtered_vacancies = []
        for item in data:
            vacancy = Vacancy(**item)
            if criteria['title'].lower() in vacancy.title.lower():
                salary_from = vacancy.salary.get('from') if vacancy.salary else 0
                salary_to = vacancy.salary.get('to') if vacancy.salary else float('inf')
                if (salary_from is None or salary_from >= criteria['salary_from']) and (
                        salary_to is None or salary_to <= criteria['salary_to']):
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаляет вакансию из JSON-файла.
        """
        data = self._load_data()
        data = [item for item in data if item['title'] != vacancy.title]
        self._save_data(data)

    def _load_data(self):
        """
        Загружает данные из JSON-файла.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
            return []

    def _save_data(self, data):
        """
        Сохраняет данные в JSON-файл.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
