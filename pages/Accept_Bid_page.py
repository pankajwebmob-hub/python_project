from playwright.sync_api import Page

class Accept_Bid:
    def __init__(self,page: Page):
        self.page = page
        self.respond_button = page.get_by_role("button", name="Respond")
        self.accept_button = page.get_by_role("button", name="Accept")

    def respond_popup(self):
        self.respond_button.click()

    def accept_bid_request(self):
        self.accept_button.click()