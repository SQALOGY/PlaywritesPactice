from playwright.sync_api import sync_playwright
import time

def test_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_context(no_viewport=True).new_page()
        page.goto("https://demoqa.com/select-menu")
        time.sleep(2)

        # Select by visible text
        page.locator("#oldSelectMenu").select_option(label="Blue")

        selected = page.locator("#oldSelectMenu").input_value()
        print("Selected value:", selected)

        time.sleep(5)

        browser.close()

def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_context(no_viewport=True).new_page()
        page.goto("https://www.saucedemo.com")
        time.sleep(2)


        # Full page screenshot
        page.screenshot(path="screenshots/full_page.png", full_page=True)
        print("Screenshot saved!")

        browser.close()

def test_element_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_context(no_viewport=True).new_page()
        page.goto("https://www.saucedemo.com")
        time.sleep(2)

        # Screenshot of just the login button
        page.locator(".btn_action").screenshot(
            path="screenshots/login_button.png"
        )
        print("Element screenshot saved!")

        browser.close()

def test_with_screenshot_on_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )
        page = browser.new_context(no_viewport=True).new_page()
        time.sleep(2)
        try:
            page.goto("https://www.saucedemo.com")
            page.get_by_placeholder("Username").fill("wrong_user")
            page.get_by_placeholder("Password").fill("wrong_pass")
            page.get_by_role("button", name="Login").click()

            assert "inventory" in page.url

        except AssertionError:
            page.screenshot(path="screenshots/failure.png")
            print("Test failed — screenshot captured!")
            raise

        finally:
            browser.close()