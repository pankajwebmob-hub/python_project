from playwright.sync_api import Page


class initiate_Bid:
    def __init__(self, page: Page):
        self.page = page
        self.initiate_bid = page.locator("#term-tour0").get_by_text("Mio")
        self.rate_button = page.get_by_role("button", name="%")
        self.initiate_button = page.get_by_role("button", name="Initiate")

    def Initiate_popup(self):
        self.initiate_bid.click()

    def Initiate_rate(self):
        self.rate_button.click()

    def Initiate_Bid_Request(self):
        self.initiate_button.click()
