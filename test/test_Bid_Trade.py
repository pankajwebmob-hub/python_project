from utils.credentials import get_credentials
import time
from playwright.sync_api import expect
from playwright.sync_api import Page
from pages.IM_login_page import LoginPage
from pages.Create_Bid_page import create_Bid


def test_login(page: Page) -> None:
# User Login:
    login_page = LoginPage(page)
    creds = get_credentials()

    login_page.navigate()
    login_page.enter_username(creds["username"])
    login_page.enter_password(creds["password"])
    login_page.click_login()
    time.sleep(10)

# Create Bid:
    create_bid = create_Bid(page)
    create_bid.Bid_popup()
    create_bid.enter_amount("6")
    create_bid.enter_rate("2")
    create_bid.submit_button()

# Assert success message is visible:
    success_message = page.locator("text=Request created successfully")
    expect(success_message).to_be_visible()





    # page.locator("#bid-offer-tour0").get_by_role("button", name="Bid").click()
    # page.get_by_role("textbox", name="Text input with dropdown").click()
    # page.get_by_role("textbox", name="Text input with dropdown").fill("8")
    # page.get_by_role("textbox", name="Enter rate").click()
    # page.get_by_role("textbox", name="Enter rate").fill("3")
    # page.get_by_role("button", name="Submit Quote").click()



