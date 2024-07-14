import re


class Vacancy:
    """
    Класс, представляющий вакансию.
    """

    def __init__(self, title: str, url: str, salary: dict, description: str):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

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