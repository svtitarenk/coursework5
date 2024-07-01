from utils.utils import create_database, create_tables, insert_data_into_tables
from classes.db_manager import DBManager

db_name = "coursework"
create_database(db_name)
create_tables(db_name)
insert_data_into_tables(db_name)


while True:
    print("")
    print("--------------------------------------------")
    print("1: Вывод всех компаний и количества вакансий")  # get_companies_and_vacancies_count()
    print("2: Вывод всех компаний и вакансий (название, ЗП, url")
    print("3: Вывод средней зарплаты по вакансиям")
    print("4: Вывод вакансий с зарплатой выше средней")
    print("5: Вывод вакансий в названии, которой есть ключевое слово")
    print("6: Выход")
    print("--------------------------------------------")
    print("")

    db = DBManager(db_name)

    answer = int(input())
    if answer == 6:
        break
    elif answer == 1:
        print(*db.get_companies_and_vacancies_count(), sep="\n")
    elif answer == 2:
        print(*db.get_all_vacancies(), sep="\n")
    elif answer == 3:
        print(*db.get_avg_salary(), sep="\n")
    elif answer == 4:
        print(*db.get_vacancies_with_higher_salary(), sep="\n")
    elif answer == 5:
        keyword = input("Введите ключевое слово для поиска: ").lower()
        print(*db.get_vacancies_with_keyword(keyword), sep="\n")
