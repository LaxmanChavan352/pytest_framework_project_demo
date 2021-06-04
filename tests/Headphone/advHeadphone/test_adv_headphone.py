from pytest import mark
@mark.smoke
@mark.fix
def test_adv_headphone_testing(get_browser):
    driver=get_browser
    driver.get("https://www.google.com/search?client=firefox-b-d&q=google")
    assert True