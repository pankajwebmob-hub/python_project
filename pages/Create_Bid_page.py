from playwright.sync_api import Page
class create_Bid:
    def __init__(self, page:Page):
        self.page = page
        self.click_bid = page.locator("#bid-offer-tour0").get_by_role("button", name="Bid")
        self.amount_input = page.get_by_role("textbox", name="Text input with dropdown")
        self.rate_input = page.get_by_role("textbox", name="Enter rate")
        self.submit_quote = page.get_by_role("button", name="Submit Quote")

    def Bid_popup(self):
        self.click_bid.click()


    def enter_amount(self, amount: str):
        self.amount_input.click()
        self.amount_input.fill("")
        self.amount_input.type(amount)
        self.amount_input.press("Tab")

    def enter_rate(self, rate: str):
        self.rate_input.click()
        self.rate_input.fill("")
        self.rate_input.type(rate)
        self.rate_input.press("Tab")

    def submit_button(self):
        self.submit_quote.click()
