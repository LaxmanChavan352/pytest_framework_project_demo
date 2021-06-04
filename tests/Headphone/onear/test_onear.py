from selenium import webdriver
from pytest import mark
@mark.fix
@mark.headpone
def test_onear_testing(get_browser):
    get_browser.get("https://www.boat-lifestyle.com/products/rockerz-550?variant=31352999444578&currency=INR&gclid=Cj0KCQjw--GFBhDeARIsACH_kdbVOYbe8XyhHy0aQk-egWw8DBtSszZGNOYPw00vGJ3zhfSV-r4o7T4aAq75EALw_wcB")
    assert True