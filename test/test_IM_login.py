import time

from playwright.sync_api import Page
from pages.IM_login_page import LoginPage
def test_Valid_login(page: Page) -> None:
    login_page = LoginPage(page)

    page.goto("https://testing.instimatch.ch")
    login_page.enter_username("hsagar01")
    login_page.enter_password("Wpadmin@0001")
    login_page.click_login()
    login_page.click_logout()
    assert login_page.is_logged_out(), "Logout failed: Sign In button not visible"
    page.screenshot(path="screenshots/login_success.png")
    time.sleep(3)

def test_Invalid_login(page: Page):
    login_page = LoginPage(page)

    page.goto("https://testing.instimatch.ch")
    login_page.enter_username("hsagar")
    login_page.enter_password("123")
    login_page.click_login()
    assert login_page.is_error_message_displayed("Username/Password did not match, please try again"), "Error message missing for invalid credentials"
    page.screenshot(path="screenshots/login_success.png")
    time.sleep(3)

def test_Blank_Username_and_Password(page: Page):
    login_page = LoginPage(page)

    page.goto("https://testing.instimatch.ch")
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.is_error_message_displayed("All fields are mandatory"), "Error message not shown for blank credentials"
    page.screenshot(path="screenshots/login_success.png")
