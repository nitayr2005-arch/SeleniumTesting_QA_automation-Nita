# pages/dashboard_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    URL = 'https://the-internet.herokuapp.com/secure'

    # ── Locators ──────────────────────────────────────
    LOGOUT_BTN  = (By.CSS_SELECTOR, 'a[href="/logout"]')
    DASHBOARD_HEADER = (By.TAG_NAME, 'h2')

    # ── Actions ───────────────────────────────────────
    def logout(self):
        self.logger.info('Klik tombol Logout')
        self.click(self.LOGOUT_BTN)

    # ── Assertion Helpers ─────────────────────────────
    def is_on_dashboard(self):
        """Return True jika user sedang berada di halaman dashboard"""
        return self.get_current_url() == self.URL and \
               self.is_visible(self.LOGOUT_BTN)