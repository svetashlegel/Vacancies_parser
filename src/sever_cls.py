from abc import ABC, abstractmethod
import json
from src.vacancy_cls import Vacancy


class VacanciesSever(ABC):
    """Абстрактный класс для сохранения и работы с файлами вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        """Возвращает вакансии, соответствующие уровню зарплаты"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаляет вакансию"""
        pass


class JSONSever(VacanciesSever):
    """Класс для работы с json-файлами"""

    def __init__(self, vacancy_name):
        self.file = f'{vacancy_name}.json'

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump([], file)

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        with open(self.file, 'r', encoding='utf-8') as file:
            data_vacancies = json.load(file)
            data_vacancies.append(vacancy.__dict__)
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data_vacancies, file)

    def get_vacancies_by_salary(self, salary):
        """Возвращает вакансии, соответствующие уровню зарплаты"""
        vacancies = []
        salary_min = int(salary.split('-')[0])
        salary_max = int(salary.split('-')[1])
        with open(self.file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not data:
                print(f"По запросу '{self.vacancy}' вакансий не найдено")
                exit()
            else:
                for i in data:
                    vacancy = Vacancy(i['vacancy'], i['company'], i['salary'], i['employment'], i['experience'],
                                        i['requirements'], i['url'], i['platform'])
                    if salary_min <= vacancy.salary <= salary_max:
                        vacancies.append(vacancy)
        if not vacancies:
            print("В соответствии с установленным уровнем заработной платы вакансий не найдено")
        else:
            return vacancies

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию"""
        with open(self.file, 'r', encoding='utf-8') as file:
            data_vacancies = json.load(file)
            counter = 0
            for item in data_vacancies:
                if item['vacancy'] == vacancy.vacancy:
                    data_vacancies.pop(counter)
                else:
                    counter += 1

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data_vacancies, file)
