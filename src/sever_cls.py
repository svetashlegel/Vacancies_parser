import json
from abc import ABC, abstractmethod
from src.vacancy_cls import Vacancy


class VacanciesSever(ABC):
    """Абстрактный класс для сохранения и работы с файлами вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Возвращает все доступные вакансии"""
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        """Возвращает вакансии, соответствующие уровню зарплаты"""
        pass

    @abstractmethod
    def get_vacancies_by_employment(self, employment):
        """Возвращает вакансии, соответствующие выбранному типу занятости"""
        pass

    @abstractmethod
    def get_vacancies_by_experience(self, experience):
        """Возвращает вакансии, соответствующие выбранному типу занятости"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаляет вакансию"""
        pass


class JSONSever(VacanciesSever):
    """Класс для работы с json-файлами"""

    def __init__(self, vacancy_name):
        self.vacancy = vacancy_name
        self.file = f'{vacancy_name}.json'

        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump([], file)

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл json"""
        with open(self.file, 'r', encoding='utf-8') as file:
            data_vacancies = json.load(file)
            data_vacancies.append(vacancy.__dict__)
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data_vacancies, file)

    def get_vacancies(self):
        """Возвращает все доступные вакансии"""
        vacancies = []
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    print(f"По запросу '{self.vacancy}' вакансий не найдено")
                    exit()
                else:
                    for i in data:
                        vacancy = Vacancy(i['vacancy'], i['company'], i['salary'], i['employment'], i['experience'],
                                          i['requirements'], i['url'], i['platform'])
                        vacancies.append(vacancy)
                return vacancies
        except FileNotFoundError:
            print("Файл не найден")

    def get_vacancies_by_salary(self, salary):
        """Возвращает вакансии, соответствующие уровню зарплаты"""
        vacancies = []
        try:
            salary_min = int(salary.split('-')[0])
            salary_max = int(salary.split('-')[1])
        except ValueError:
            print("Ошибка распознования: данные введены не в числовом формате")
            exit()
        except IndexError:
            print("Ошибка распознования: данные введены не в формате min-max")
            exit()
        else:
            try:
                with open(self.file, 'r', encoding='utf-8') as file:
                    data = json.load(file)
            except FileNotFoundError:
                print("Файл не найден")
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

    def get_vacancies_by_employment(self, employment):
        """Возвращает вакансии, соответствующие выбранному типу занятости"""
        if employment == 1:
            emp_criterion = ['Полный рабочий день', 'Полная занятость']
        elif employment == 2:
            emp_criterion = ['Неполная дистанционная занятость', 'Частичная занятость']
        else:
            print("Ошибка распознавания: выбранный номер отсутствует в списке")
            exit()
        vacancies = []
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    print(f"По запросу '{self.vacancy}' вакансий не найдено")
                    exit()
                else:
                    for i in data:
                        vacancy = Vacancy(i['vacancy'], i['company'], i['salary'], i['employment'], i['experience'],
                                          i['requirements'], i['url'], i['platform'])
                        if vacancy.employment in emp_criterion:
                            vacancies.append(vacancy)
                return vacancies
        except FileNotFoundError:
            print("Файл не найден")

    def get_vacancies_by_experience(self, experience):
        """Возвращает вакансии, соответствующие выбранному типу занятости"""
        if experience == 1:
            exp_criterion = ['Нет опыта', 'Без опыта', 'Не имеет значения']
        elif experience == 2:
            exp_criterion = ['От 1 года', 'От 1 года до 3 лет', 'Не имеет значения']
        elif experience == 3:
            exp_criterion = ['От 3 до 6 лет', 'От 3 лет', 'Не имеет значения']
        elif experience == 4:
            exp_criterion = ['Более 6 лет', 'От 3 лет', 'Не имеет значения']
        else:
            print("Ошибка распознавания: выбранный номер отсутствует в списке")
            exit()
        vacancies = []
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if not data:
                    print(f"По запросу '{self.vacancy}' вакансий не найдено")
                    exit()
                else:
                    for i in data:
                        vacancy = Vacancy(i['vacancy'], i['company'], i['salary'], i['employment'], i['experience'],
                                          i['requirements'], i['url'], i['platform'])
                        if vacancy.experience in exp_criterion:
                            vacancies.append(vacancy)
                return vacancies
        except FileNotFoundError:
            print("Файл не найден")

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию"""
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data_vacancies = json.load(file)
                counter = 0
                for item in data_vacancies:
                    if item['vacancy'] == vacancy.vacancy:
                        data_vacancies.pop(counter)
                    else:
                        counter += 1
        except FileNotFoundError:
            print("Файл не найден")
        else:
            with open(self.file, 'w', encoding='utf-8') as file:
                json.dump(data_vacancies, file)
