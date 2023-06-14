class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, vacancy, company, salary, employment, experience, requirements, url, platform):
        self.vacancy = vacancy
        self.company = company
        self.employment = employment
        self.experience = experience
        self.requirements = requirements
        self.url = url
        self.salary = int(salary)
        self.platform = platform

    def __str__(self):
        """Представление вакансии для пользователя"""
        return f"Вакансия: {self.vacancy}\n" \
               f"Компания: {self.company}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Требования: {self.requirements}\n" \
               f"Ссылка на вакансию: {self.url}"
    