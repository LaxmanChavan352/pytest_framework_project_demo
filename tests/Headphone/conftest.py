from selenium import webdriver
from pytest import fixture
@fixture(scope='function')
def get_browser():
    driver = webdriver.Chrome(executable_path="C:\\Apps\\chromedriver.exe")
    return driver