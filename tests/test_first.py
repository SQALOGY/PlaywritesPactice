from playwright.sync_api import sync_playwright
import time

def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(  
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_context(no_viewport=True).new_page()
        page.goto("https://www.saucedemo.com")
        print(page.title())
        time.sleep(5)
        browser.close()

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"])
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()
        time.sleep(5)

        assert "inventory" in page.url
        print("Login successful!")

        browser.close()