from abc import ABC, abstractmethod


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

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        pass

    def get_vacancies_by_salary(self, salary):
        """Возвращает вакансии, соответствующие уровню зарплаты"""
        pass

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию"""
        pass
