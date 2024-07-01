import psycopg2
from config import config
import os
from config import ROOT_DIR
import json

params_file_name = os.path.join(ROOT_DIR, 'database.ini')

params = config(params_file_name)


class DBManager:
    def __init__(self, name):
        self.__name = name

    def __execute_query(self, query):
        """ приватный метод для исполнения query запросов, возвращает результат запроса SQL """
        conn = psycopg2.connect(dbname=self.__name, **params)

        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

        conn.close()
        return result

    def get_all(self):
        """ получить все вакансии - тестовый """
        return self.__execute_query(""" SELECT * FROM vacancies """)

    def get_companies_and_vacancies_count(self):
        """ Получить компании и количество вакансий у них """
        return self.__execute_query(""" SELECT employers.name, count(*) FROM vacancies
         LEFT JOIN employers on vacancies.employer = employers.id
         GROUP BY employers.name
         """)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        return self.__execute_query(""" SELECT employers.name, vacancies.name, vacancies.salary_from, vacancies.url FROM vacancies
         LEFT JOIN employers on vacancies.employer = employers.id  """)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        result = self.__execute_query("""SELECT name, round(avg(salary_from),2) as salary 
        from vacancies 
        GROUP BY name 
        ORDER BY round(avg(salary_from),2) desc, name
        """)
        return result

    def get_vacancies_with_higher_salary(self):
        """ получает список всех вакансий, у которых зарплата выше средней по всем вакансиям """
        result = self.__execute_query("""SELECT name, round(salary_from,2) as salary
        from vacancies 
        where  salary_from >= (select round(avg(salary_from),2) as salary_from from vacancies)
        ORDER BY round(salary_from,2) desc      
        """)
        return result

    def get_vacancies_with_keyword(self, keyword):
        """ получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python """
        result = self.__execute_query(f"SELECT name, round(salary_from,2) as salary from vacancies where  lower(name) "
                                      f"like '%{keyword}%' order by round(salary_from,2) desc")
        return result




if __name__ == '__main__':
    db = DBManager("coursework")
    # print(json.dumps(db.get_all(), ensure_ascii=False, indent=4))
    # print(db.get_companies_and_vacancies_count()[0:3])
    # print(*db.get_all_vacancies(), sep="\n")
    # print(*db.get_avg_salary(), sep="\n")
    # print(*db.get_vacancies_with_higher_salary(), sep="\n")
    # print(*db.get_vacancies_with_keyword("продавец"), sep="\n")
