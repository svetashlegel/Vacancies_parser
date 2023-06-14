from abc import ABC, abstractmethod
import requests
import json
import os


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

        params = {
            'text': f'name:{user_request}',
            'area': 1
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        data = req.content.decode()
        req.close()
        dataj = json.loads(data)
        return dataj


class SuperJobAPI(SearchAPI):
    """Класс для работы с API SuperJob"""

    def get_vacancies(self, user_request):
        """Получает список вакансий"""

        api_key = os.getenv("SJ_API_KEY")
        params = {
            'keyword': f'{user_request}',
            'area': 1
        }
        headers = {'X-Api-App-Id': api_key}
        req = requests.get('https://api.superjob.ru/2.0/vacancies',
                           params=params, headers=headers)
        data = req.content.decode()
        req.close()
        dataj = json.loads(data)
        return dataj
