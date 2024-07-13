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
        return [Vacancy(**item) for item in data]

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
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self, data):
        """
        Сохраняет данные в JSON-файл.
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
