import requests
import json

class HHParser:
    """ отправляем запрос и получаем компании из https""//api.hh.ru/employers
    per_page
    sort_by
    """

    def __get_request(self):
        params = {"per_page": 10,
                  "sort_by": "by_vacancies_open"}
        response = requests.get("https://api.hh.ru/employers", params=params)

        if response.status_code == 200:
            return response.json()['items']

    def get_employers(self):
        """ получаем компании """
        employers = []
        data = self.__get_request()
        for employer in data:
            employers.append({"id": employer["id"], "name": employer["name"]})
        return employers

    def __get_vacancies_on_employer(self, id):
        """
        получим все вакансии по списку компаний по параметру поля employer_id
        передаем один id компании
        возвращает список вакансий по переданному ID
        """
        params = {"employer_id": id,
                  'currency': 'RUR',
                  'only_with_salary': True
                  }
        response = requests.get("https://api.hh.ru/vacancies", params=params)
        if response.status_code == 200:
            return response.json()["items"]

    def get_all_vacancies(self):
        """ получаем весь список вакансий по id компании и возвращаем список словарей"""
        employers = self.get_employers()
        all_vacancies = []
        for employer in employers: # перебираем компании
            vacancies = self.__get_vacancies_on_employer(employer["id"])
            for vacancy in vacancies: # перебираем у каждого работодателя все открытые вакансии
                if vacancy["salary"] is None: # проверка на пустую зарплату
                    salary_from = 0
                    salary_to = 0
                else:
                    salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                    salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
                all_vacancies.append({"id": vacancy["id"],
                                      "name": vacancy["name"],
                                      "url": vacancy["alternate_url"],
                                      "salary_from": salary_from,
                                      "salary_to": salary_to,
                                      "employer": employer["id"],
                                      "city": vacancy["area"]["name"],
                                      "experience": vacancy["experience"]["name"]
                                      })
        return all_vacancies

if __name__ == '__main__':

    hh = HHParser()
    # print(hh.get_employers())
    # print(json.dumps(hh.get_all_vacancies(), ensure_ascii=False, indent=4) )
