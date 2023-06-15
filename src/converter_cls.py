from abc import ABC, abstractmethod


class DataConverter(ABC):
    """Абстрактный класс для приведения информации к нужному виду"""

    @abstractmethod
    def convert_data(self, i):
        """Приводит информацию к нужному виду"""
        pass


class HeadHunterConverter(DataConverter):
    """Преобразует данные, полученные с headhunter"""

    def convert_data(self, i):
        """Преобразует данные по вакансии для создания экземпляра класса Vacancy"""
        try:
            url = f"https://hh.ru/vacancy/{i['id']}"
            if i['salary']['from'] and i['salary']['from'] != 0:
                salary = i['salary']['from']
            else:
                salary = i['salary']['to']
            data = [i['name'], i['employer']['name'], salary, i['employment']['name'], i['experience']['name'],
                    i['snippet']['requirement'], url, 'HeadHunter']
        except TypeError:
            pass
        else:
            return data


class SuperJobConverter(DataConverter):
    """Преобразует данные, полученные с superjob"""

    def convert_data(self, i):
        """Преобразует данные по вакансии для создания экземпляра класса Vacancy"""
        try:
            requirement = i['candidat'].split('Требования:')[1].split('Условия:')[0]
            if i['payment_from'] and i['payment_from'] != 0:
                salary = i['payment_from']
            else:
                salary = i['payment_to']
            data = [i['profession'], i['client']['title'], salary, i['type_of_work']['title'],
                    i['experience']['title'], requirement, i['link'], 'SuperJob']
        except IndexError:
            pass
        except KeyError:
            pass
        else:
            return data
