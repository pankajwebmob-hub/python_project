import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://testing.instimatch.ch/")
    page.get_by_role("textbox", name="Enter your username").fill("hsagar01")
    page.get_by_role("textbox", name="Enter your password").fill("Wpadmin@0001")
    page.get_by_role("button", name="Sign Me In").click()
    page.locator("#companyDetailsDropdown").click()
    page.locator("a").filter(has_text="Log Out").click()
    page.get_by_role("button", name="Yes").click()