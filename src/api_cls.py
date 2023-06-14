from abc import ABC, abstractmethod


class SearchAPI(ABC):
    """Абстрактный класс для работы с API сайтов"""

    @abstractmethod
    def get_vacancies(self, user_request):
        """Получает список вакансий"""
        pass


class HeadHunterAPI(SearchAPI):
    """Класс для работы с API HeadHunter"""

    def get_vacancies(self, user_request):
        """Получает список вакансий"""
        pass


class SuperJobAPI(SearchAPI):
    """Класс для работы с API SuperJob"""

    def get_vacancies(self, user_request):
        """Получает список вакансий"""
        pass
