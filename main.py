from src.api_cls import HeadHunterAPI, SuperJobAPI
from src.vacancy_cls import Vacancy
from src.sever_cls import JSONSever
from src.converter_cls import HeadHunterConverter, SuperJobConverter
from src.user_interraction_func import get_search_query


hh_api = HeadHunterAPI()
hh_converter = HeadHunterConverter
superjob_api = SuperJobAPI()
sj_converter = SuperJobConverter

search_query = get_search_query()
json_sever = JSONSever(search_query)

data_hh = hh_api.get_vacancies(search_query)
for i in data_hh['items']:
    data = hh_converter.convert_data(data_hh, i)
    if data:
        vacancy = Vacancy(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        json_sever.add_vacancy(vacancy)

data_sj = superjob_api.get_vacancies(search_query)
for i in data_sj['objects']:
    data = sj_converter.convert_data(data_sj, i)
    if data:
        vacancy = Vacancy(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        json_sever.add_vacancy(vacancy)
