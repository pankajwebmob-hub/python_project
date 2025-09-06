from playwright.sync_api import Page, expect
class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Enter your username")
        self.password_input = page.get_by_role("textbox", name="Enter your password")
        self.SignMeIn_button = page.get_by_role("button", name="Sign Me In")
        self.profile_menu = page.locator("#companyDetailsDropdown")
        self.logout_link = page.locator("a").filter(has_text="Log Out")
        self.confirm_logout_button = page.get_by_role("button", name="Yes")

    def enter_username(self, username: str):
        self.username_input.fill(username)
    def enter_password(self, password: str):
        self.password_input.fill(password)
    def click_login(self):
        self.SignMeIn_button.click()
    def click_logout(self):
        self.profile_menu.click()
        self.logout_link.click()
        self.confirm_logout_button.click()

    def is_logged_out(self):
        return expect(self.SignMeIn_button).to_be_visible()
