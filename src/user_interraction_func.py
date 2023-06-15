from src.vacancy_cls import Vacancy


def get_search_query():
    """Фунция получает запрос пользователя"""
    search_query = input("Введите поисковый запрос: ")
    return search_query


def get_filtered_list(json_sever):
    """Функция возвращает фильтрованый список вакансий в соответствии с запросом пользователя"""
    print("Фильтровать вакансии:\n1 - по зарплате;\n2 - по типу занятости;\n3 - по опыту работы;\n4- все вакансии."
          "\nВыберите соответствующий номер")
    filtr_criterion = input()
    if int(filtr_criterion) == 1:
        print("Введите уровень зарплаты в формате min-max:")
        salary_crit = input()
        filtered_vacancies = json_sever.get_vacancies_by_salary(salary_crit)
    elif int(filtr_criterion) == 2:
        print("Выберите тип занятости:\n1 - полная занятость;\n2 - частичная занятость."
              "\nУкажитесоответствующий номер")
        emp_crit = int(input())
        filtered_vacancies = json_sever.get_vacancies_by_employment(emp_crit)
    elif int(filtr_criterion) == 3:
        print("Ваш опыт работы:\n1 - нет опыта работы;\n2 - от 1 года до 3 лет;"
              "\n3 - от 3 до 6 лет;\n4 - более 6 лет.\nВыберите соответствующий номер")
        exp_crit = int(input())
        filtered_vacancies = json_sever.get_vacancies_by_experience(exp_crit)
    elif int(filtr_criterion) == 4:
        filtered_vacancies = json_sever.get_vacancies()
    else:
        print("Невозможно интерпретировать ответ, фильтр не был применен")
        filtered_vacancies = json_sever.get_vacancies()
    return filtered_vacancies


def get_sorted_list(filtered_vacancies):
    """Функция возвращает сортированный топ N вакансий в соответствии с запросом пользователя"""
    sorted_list = Vacancy.sort_by_salary(filtered_vacancies)
    top = int(input("Вывести топ N вакансий: "))
    final_list = Vacancy.get_top_vacancies(sorted_list, top)
    return final_list


def define_platform(vacancies_list):
    """Возвращает список вакансий в соответствии с выбранной платформой"""
    user_input = input("Выберите с какой платформы вакансии Вас интересуют:\n1 - HeadHunter;"
                       "\n2 - SuperJob;\n3 - все платформы.\nВыберите соответствующий номер")
    if int(user_input) == 1:
        platform = 'HeadHunter'
        filtered_list = Vacancy.get_vacancies_by_platform(vacancies_list, platform)
    elif int(user_input) == 2:
        platform = 'SuperJob'
        filtered_list = Vacancy.get_vacancies_by_platform(vacancies_list, platform)
    elif int(user_input) == 3:
        filtered_list = vacancies_list
    else:
        print("Не удалось распознать ответ, фильтр не применен")
        filtered_list = vacancies_list
    return filtered_list
