import re

class Vacancy:
    """
    Класс, представляющий вакансию.
    """
    def __init__(self, title: str, url: str, salary: dict = None, description: str = ''):
        self.title = title
        self.url = url
        self.salary = salary if salary is not None else {}
        self.description = self.clean_description(description or '')
        self.validate()

    def __str__(self):
        salary_from = self.salary.get('from') if self.salary else None
        salary_to = self.salary.get('to') if self.salary else None
        salary_currency = self.salary.get('currency') if self.salary else None
        salary_str = f"{salary_from} - {salary_to} {salary_currency}" if salary_from and salary_to else "Не указана"
        return f"{self.title} - {salary_str}\n{self.url}\n{self.description}"

    def get_salary(self):
        return self.salary.get('from') if self.salary and self.salary.get('from') else 0

    def clean_description(self, description: str) -> str:
        return re.sub(r'<highlighttext>|</highlighttext>', '', description)

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.title == other.title and self.url == other.url

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary() < other.get_salary()

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary() <= other.get_salary()

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary() > other.get_salary()

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary() >= other.get_salary()

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary() != other.get_salary()

    def validate(self):
        if not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой.")
        if not isinstance(self.url, str):
            raise ValueError("URL должен быть строкой.")
        if not isinstance(self.salary, dict):
            raise ValueError("Зарплата должна быть представлена в виде словаря.")
        if not isinstance(self.description, str):
            raise ValueError("Описание должно быть строкой.")
        if self.salary:
            if 'from' in self.salary and self.salary['from'] is not None and not isinstance(self.salary['from'], (int, float)):
                raise ValueError("Зарплата 'from' должна быть числом.")
            if 'to' in self.salary and self.salary['to'] is not None and not isinstance(self.salary['to'], (int, float)):
                raise ValueError("Зарплата 'to' должна быть числом.")
            if 'currency' in self.salary and not isinstance(self.salary['currency'], str):
                raise ValueError("Валюта должна быть строкой.")









