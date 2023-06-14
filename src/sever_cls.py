from abc import ABC, abstractmethod
import json


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
        pass

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
