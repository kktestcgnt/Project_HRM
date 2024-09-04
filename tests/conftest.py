import configparser

import psycopg2
import pymongo

import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from common.common import BaseClass


@pytest.fixture()
def multiple_window_setup(request):
    read_data = BaseClass()
    login_creds = read_data.get_data()

    app_url = login_creds['app_login_page']["app_url"]

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get(app_url)
    time.sleep(5)

    # request.cls.driver = driver
    print("Driver from Fixture : ", driver)

    return driver

    # yield
    # add teardown code


@pytest.fixture()
def alerts_setup():
    read_data = BaseClass()
    login_creds = read_data.get_data()

    app_url = login_creds['alerts_page']["alerts_app_url"]

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get(app_url)
    time.sleep(5)

    print("Driver from Fixture : ", driver)
    return driver


@pytest.fixture()
def bar_pie_charts_setup():
    read_data = BaseClass()
    login_creds = read_data.get_data()

    app_url = login_creds['bar_pie_charts_page']["bar_pie_charts_app_url"]

    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)

    driver.maximize_window()
    driver.get(app_url)
    time.sleep(5)

    print("Driver from Fixture : ", driver)
    return driver


@pytest.fixture()
def mongodb_connection(request):
    class MongoDB:

        @staticmethod
        def establishing_connection(db_name=request.param[0], col_name=request.param[1]):
            url = "mongodb://192.168.29.72:27017/"
            mongo_client = pymongo.MongoClient(url)
            print("Connection is Successful")

            # Connect to an existing Collection in Database
            mongo_cursor = mongo_client[db_name][col_name]
            print('\nFixture Cursor : ', mongo_cursor)
            return mongo_cursor

    obj_mongodb = MongoDB().establishing_connection()
    return obj_mongodb


def establishing_inifile_connection(inifile_path):

    ini_cursor = configparser.ConfigParser()
    print("\n", inifile_path)
    ini_cursor.read(inifile_path)
    # data.read("E:/python_projects/Project_HRM/data/data.ini")
    print("in fixture : ", ini_cursor.sections())
    return ini_cursor


@pytest.fixture()
def inifile_connection(request):
    print('\nin fixture - ', request.param[0])
    print(request.param[0]['app_login_page'])
    inifile_pointer = establishing_inifile_connection(request.param[0])
    return inifile_pointer


# postgresql = {'postgresql_connection': None, 'postgresql_pointer': 0}
postgresql = {}


@pytest.fixture()
def postgresql_connection():
    global postgresql

    def establishing_connection():
        global postgresql
        hostname = '192.168.29.72'
        database = 'testdb'
        username = 'postgres'
        password = 'postgres'
        port = 5432

        postgresql['db_connection'] = psycopg2.connect(host=hostname,
                                                       dbname=database,
                                                       user=username,
                                                       password=password,
                                                       port=port)
        print(postgresql['db_connection'])  # Add Assert statement here.
        print("Connection is Successful")

        postgresql['db_cursor'] = postgresql['db_connection'].cursor()

        return postgresql['db_cursor']

    yield establishing_connection()
    postgresql['db_cursor'].close()
    postgresql['db_connection'].close()
