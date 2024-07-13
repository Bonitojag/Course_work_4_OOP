class Vacancy:
    """
    Класс, представляющий вакансию.
    """

    def __init__(self, title: str, url: str, salary: str, description: str):
        """
        Инициализирует вакансию с заданными параметрами.
        Название вакансии
        Ссылка на вакансию
        З/п
        Описание вакансии
        """
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление вакансии.

        """
        return f"{self.title} - {self.salary}\n{self.url}\n{self.description}"

    def __lt__(self, other):
        """
        Сравнивает вакансии по зарплате (меньше).
        """
        return self.salary < other.salary

    def __gt__(self, other):
        """
        Сравнивает вакансии по зарплате (больше).
        """
        return self.salary > other.salary