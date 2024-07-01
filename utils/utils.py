import psycopg2
from config import config
import os
from config import ROOT_DIR
from classes.hh_parser import HHParser

params_file_name = os.path.join(ROOT_DIR, 'database.ini')

params = config(params_file_name)


# print(params["host"])


def create_database(db_name: str):
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    cur.close()
    conn.close()


def create_tables(db_name):
    conn = psycopg2.connect(dbname=db_name, **params)

    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE employers (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL
        )
        """)

        cur.execute("""CREATE TABLE vacancies (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        url VARCHAR(100),
        salary_from INTEGER,
        salary_to INTEGER,
        employer INTEGER REFERENCES employers (id),
        city VARCHAR(100),
        experience VARCHAR(255)
        )
        """)

    conn.close()


def insert_data_into_tables(db_name):
    hh = HHParser()
    employers = hh.get_employers()
    vacancies = hh.get_all_vacancies()
    conn = psycopg2.connect(dbname=db_name, **params)

    with conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            for employer in employers:
                cur.execute(""" INSERT INTO employers VALUES (%s, %s) """, (employer["id"], employer["name"]))
            for vacancy in vacancies:
                cur.execute(""" INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """,
                            (vacancy["id"],
                             vacancy["name"],
                             vacancy["url"],
                             vacancy["salary_from"],
                             vacancy["salary_to"],
                             vacancy["employer"],
                             vacancy["city"],
                             vacancy["experience"]
                             ))

    conn.close()


if __name__ == '__main__':
    create_tables("coursework")
