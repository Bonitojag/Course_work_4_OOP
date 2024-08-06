def parse_salary_range(salary_range: str):
    if salary_range:
        if '-' in salary_range:
            salary_from, salary_to = map(int, salary_range.split('-'))
        else:
            salary_from = int(salary_range)
            salary_to = float('inf')
    else:
        salary_from = 0
        salary_to = float('inf')
    return salary_from, salary_to


