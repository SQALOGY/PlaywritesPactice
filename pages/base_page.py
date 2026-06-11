from pages.page_interface import PageInterface
import os
import json

class BasePage(PageInterface):
    """
    BasePage — implements PageInterface contract
    and adds common utility methods
    """
     
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)
        print(f"🌐 Opened URL: {url}")

    def is_loaded(self):
        return self.page.url is not None

    def get_page_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def take_screenshot(self, filename):
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        self.page.screenshot(
            path=f"{screenshots_dir}/{filename}.png",
            full_page=True
        )
        print(f"📸 Screenshot saved: {screenshots_dir}/{filename}.png")

    def wait(self, milliseconds):
        self.page.wait_for_timeout(milliseconds)

    @staticmethod
    def load_test_data(filename):
        filepath = os.path.join("testdata", filename)
        with open(filepath, "r") as f:
            return json.load(f)