import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Test class for Login functionality.
    All tests related to login are grouped here.
    This is OOP applied to tests.
    """

    # ===========================
    # Positive Test
    # ===========================
    def test_valid_login(self, page):
        """Test login with valid credentials"""

        # Load test data from JSON file
        test_data = LoginPage.load_test_data("login_data.json")
        valid_user = test_data["valid_user"]

        # Create LoginPage object - POM in action
        login_page = LoginPage(page)

        # Open login page
        login_page.open(valid_user["url"])
        login_page.wait(2000)

        # Perform login
        login_page.login(
            valid_user["username"],
            valid_user["password"]
        )
        login_page.wait(3000)

        # Take screenshot after login
        login_page.take_screenshot("valid_login_success")

        # Assert
        assert valid_user["expected_url"] in login_page.get_url()
        print(f"✅ Valid login test passed!")
        print(f"✅ Current URL: {login_page.get_url()}")

    # ===========================
    # Negative Test
    # ===========================
    def test_invalid_login(self, page):
        """Test login with invalid credentials"""

        # Load test data from JSON file
        test_data = LoginPage.load_test_data("login_data.json")
        invalid_user = test_data["invalid_user"]

        # Create LoginPage object
        login_page = LoginPage(page)

        # Open login page
        login_page.open(invalid_user["url"])
        login_page.wait(2000)

        # Perform login with wrong credentials
        login_page.login(
            invalid_user["username"],
            invalid_user["password"]
        )
        login_page.wait(2000)

        # Take screenshot of failure state
        login_page.take_screenshot("invalid_login_error")

        # Assert error message appears
        error_message = login_page.get_error_message()
        print(f"❌ Error message shown: {error_message}")
        assert invalid_user["expected_error"] in error_message
        print(f"✅ Invalid login test passed — error message verified!")

    # ===========================
    # Screenshot Test
    # ===========================
    def test_login_page_screenshot(self, page):
        """Take screenshot of login page before any action"""

        test_data = LoginPage.load_test_data("login_data.json")
        login_page = LoginPage(page)

        login_page.open(test_data["valid_user"]["url"])
        login_page.wait(2000)

        login_page.take_screenshot("login_page_initial")
        print(f"✅ Login page screenshot taken!")
        print(f"✅ Page title: {login_page.get_page_title()}")