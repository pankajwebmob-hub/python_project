from utils.creds import get_all_credentials
from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import expect
from playwright.sync_api import Page
from pages.IM_login_page import LoginPage
from pages.Create_Bid_page import create_Bid
from pages.Initiate_Bid_page import initiate_Bid
from pages.Accept_Bid_page import Accept_Bid

def test_full_trading_flow():
    # Load both users' credentials
    all_creds = get_all_credentials()
    creds_a = all_creds["userA"]
    creds_b = all_creds["userB"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # 1. User A logs in and creates a bid
        # ---------------------------
        context_a = browser.new_context()
        page_a = context_a.new_page()

        page_a.bring_to_front()
        login_a = LoginPage(page_a)
        login_a.navigate()
        login_a.enter_username(creds_a["username"])
        login_a.enter_password(creds_a["password"])
        login_a.click_login()


        # Create Bid:
        create_bid = create_Bid(page_a)
        create_bid.Bid_popup()
        create_bid.enter_amount("1")
        create_bid.enter_rate("2.2")
        create_bid.submit_button()
        time.sleep(2)

        # Assert success message is visible:
        expect(page_a.locator("text=Request created successfully")).to_be_visible(timeout=10000)


        # 2. User B logs in and initiates the bid
        # ---------------------------
        context_b = browser.new_context()
        page_b = context_b.new_page()

        page_b.bring_to_front()
        login_b = LoginPage(page_b)
        login_b.navigate()
        login_b.enter_username(creds_b["username"])
        login_b.enter_password(creds_b["password"])
        login_b.click_login()


        # Initiate Bid:
        initiate_bid = initiate_Bid(page_b)
        initiate_bid.Initiate_popup()
        initiate_bid.Initiate_rate()
        time.sleep(2)
        initiate_bid.Initiate_Bid_Request()
        time.sleep(2)

        # Assert request initiated successfully
        expect(page_b.locator("text=Request initiated successfully.")).to_be_visible(timeout=10000)

        # 3. Back to User A to accept the bid
        # ---------------------------
        # Refresh or navigate so User A sees the initiated bid
        page_a.reload()
        page_a.bring_to_front()

        accept_page = Accept_Bid(page_a)
        time.sleep(2)
        accept_page.respond_popup()
        accept_page.accept_bid_request()
        time.sleep(2)

        # Assert trade completed or accept success
        expect(page_a.locator("text=Trade accepted successfully.")).to_be_visible(timeout=10000)


        context_a.close()
        context_b.close()
        browser.close()





