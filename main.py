from src.vacancy import Vacancy
from src.api import HeadHunterAPI
from src.storage import JSONSaver
from src.utils import parse_salary_range


def user_interaction():
    """
    Функция для взаимодействия с пользователем.
    Позволяет вводить поисковый запрос, получать вакансии с hh.ru, сохранять их в JSON-файл и выводить на экран.
    """
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите название профессии или вакансии: ")
    salary_range = input("Введите диапазон заработной платы: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    salary_from, salary_to = parse_salary_range(salary_range)

    hh_vacancies = hh_api.get_vacancies(search_query)

    # Проверяем, что возвращенные данные являются списком
    if not isinstance(hh_vacancies, list):
        print("Ошибка: Неверный формат данных от API")
        return

    vacancies_list = [
        Vacancy(item['name'], item['alternate_url'], item['salary'], item.get('snippet', {}).get('requirement', '')) for
        item in hh_vacancies]

    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    criteria = {
        'title': search_query,
        'salary_from': salary_from,
        'salary_to': salary_to
    }

    filtered_vacancies = json_saver.get_vacancies(criteria)
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x.get_salary(), reverse=True)
    top_vacancies = sorted_vacancies[:top_n]

    print(f"\nТоп {top_n} вакансий {search_query} по зарплате:")
    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()














