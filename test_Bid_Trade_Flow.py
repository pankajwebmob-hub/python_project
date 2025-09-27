import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    page.goto("https://testing.instimatch.ch/")
    page.get_by_role("textbox", name="Enter your username").click()
    page.get_by_role("textbox", name="Enter your username").fill("hsagar01")
    page.get_by_role("textbox", name="Enter your password").click()
    page.get_by_role("textbox", name="Enter your password").fill("Wpadmin@0001")
    page.get_by_role("button", name="Sign Me In").click()
    page.locator("#bid-offer-tour1").get_by_role("button", name="Bid").click()
    page.get_by_role("textbox", name="Text input with dropdown").click()
    page.get_by_role("textbox", name="Text input with dropdown").fill("7")
    page.get_by_role("textbox", name="Enter rate").click()
    page.get_by_role("textbox", name="Enter rate").fill("3")
    page.get_by_role("button", name="Submit Quote").click()
    page1.goto("https://testing.instimatch.ch/")
    page1.get_by_role("textbox", name="Enter your username").click()
    page1.get_by_role("textbox", name="Enter your username").fill("pkumar01")
    page1.get_by_role("textbox", name="Enter your password").click()
    page1.get_by_role("textbox", name="Enter your password").fill("Wpadmin@0001")
    page1.get_by_role("button", name="Sign Me In").click()

    page1.locator("#term-tour1").get_by_text("Mio").click()
    page1.get_by_role("button", name="%").click()
    page1.get_by_role("button", name="Initiate").click()
    page.get_by_role("button", name="Respond").click()
    page.get_by_role("button", name="Accept").click()
