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
        if self.salary == 0:
            self.salary_view = 'Зарплата не указана'
        else:
            self.salary_view = self.salary
        self.platform = platform

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.vacancy}', '{self.company}', {self.salary}, {self.employment}," \
               f" {self.experience}, {self.requirements}, {self.url}, {self.platform})"

    def __str__(self):
        """Представление вакансии для пользователя"""
        return f"Вакансия: {self.vacancy}\n" \
               f"Компания: {self.company}\n" \
               f"Зарплата: {self.salary_view}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Требования: {self.requirements}\n" \
               f"Ссылка на вакансию: {self.url}"

    @staticmethod
    def sort_by_salary(vacancies_list):
        sorted_list = sorted(vacancies_list, key=lambda vacancy: vacancy.salary, reverse=True)
        return sorted_list

    @staticmethod
    def get_top_vacancies(vacancies_list, top):
        top_list = vacancies_list[0:top]
        if len(vacancies_list) <= top:
            print(f"По заданным критериям нашлось всего {len(vacancies_list)} вакансий")
        return top_list

    @staticmethod
    def get_vacancies_by_platform(vacancies_list, platform):
        filtered_list = []
        for vacancy in vacancies_list:
            if vacancy.platform == platform:
                filtered_list.append(vacancy)
        return filtered_list
