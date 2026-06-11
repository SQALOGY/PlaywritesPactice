from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object for Login Page.
    Inherits from BasePage.
    
    POLYMORPHISM in action:
    - Overrides open() to add login-specific behavior
    - Overrides is_loaded() to check login page specifically
    - Overrides get_page_title() to add custom behavior
    """

    # ===========================
    # Locators
    # ===========================

    USERNAME_INPUT = "[name='username']"
    PASSWORD_INPUT = "[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    LOGO = ".orangehrm-login-logo"

    def __init__(self, page):
        super().__init__(page)

    # ===========================
    # Polymorphism
    # Overriding parent methods
    # with specific behavior
    # ===========================

    def open(self, url):
        """
        POLYMORPHISM — overrides BasePage.open()
        Adds login page specific behavior after navigation
        """
        super().open(url)
        # Wait for login form to appear
        self.page.wait_for_selector(self.USERNAME_INPUT)
        print("✅ Login page loaded successfully!")

    def is_loaded(self):
        """
        POLYMORPHISM — overrides BasePage.is_loaded()
        Login page specific check — verifies login form exists
        """
        return self.page.locator(self.USERNAME_INPUT).is_visible()

    def get_page_title(self):
        """
        POLYMORPHISM — overrides BasePage.get_page_title()
        Login page specific title with extra info
        """
        title = super().get_page_title()
        print(f"📄 Login Page Title: {title}")
        return title
    
    
    # ===========================
    # Login Page Specific Methods
    # ===========================
    def enter_username(self, username):
        """Enter username"""
        self.page.locator(self.USERNAME_INPUT).fill(username)
        print(f"✏️ Entered username: {username}")

    def enter_password(self, password):
        """Enter password"""
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        print(f"✏️ Entered password: {'*' * len(password)}")

    def click_login(self):
        """Click login button"""
        self.page.locator(self.LOGIN_BUTTON).click()
        print("🖱️ Clicked Login button")

    def get_error_message(self):
        """Get error message text"""
        return self.page.locator(self.ERROR_MESSAGE).text_content()

    def login(self, username, password):
        """Complete login combining all steps"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()