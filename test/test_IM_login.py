from playwright.sync_api import Page
from pages.IM_login_page import LoginPage
def test_example(page: Page) -> None:
    login_page = LoginPage(page)

    page.goto("https://testing.instimatch.ch")
    login_page.enter_username("hsagar01")
    login_page.enter_password("Wpadmin@0001")
    login_page.click_login()
    login_page.click_logout()
    login_page.is_logged_out()
    page.screenshot(path="screenshots/login_success.png")
