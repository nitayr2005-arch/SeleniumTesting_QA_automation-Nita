# tests/test_login.py
import pytest
from pages.dashboard_page import DashboardPage

class TestLogin:
    # ── Test case dari modul (tetap ada) ──────────────
    def test_login_valid(self, login_page):
        login_page.login('tomsmith', 'SuperSecretPassword!')
        assert login_page.is_login_successful(), 'Login valid harus berhasil'

    def test_login_invalid_password(self, login_page):
        login_page.login('tomsmith', 'wrongpassword')
        assert login_page.is_login_failed(), 'Login dengan password salah harus gagal'

    def test_login_empty_username(self, login_page):
        login_page.login('', 'SuperSecretPassword!')
        assert login_page.is_login_failed(), 'Login tanpa username harus gagal'

    def test_flash_message_content(self, login_page):
        login_page.login('wronguser', 'wrongpass')
        msg = login_page.get_flash_message()
        assert 'invalid' in msg.lower(), f'Pesan error tidak sesuai: {msg}'

    # ── Test case baru untuk Latihan 3.1 ──────────────
    def test_user_can_logout(self, login_page):
        """Setelah login berhasil, user dapat logout"""
        # Step 1: Login dulu
        login_page.login('tomsmith', 'SuperSecretPassword!')
        assert login_page.is_login_successful(), 'Precondition gagal: login tidak berhasil'

        # Step 2: Pindah ke DashboardPage & verifikasi ada di dashboard
        dashboard = DashboardPage(login_page.driver)
        assert dashboard.is_on_dashboard(), 'User seharusnya berada di halaman dashboard'

        # Step 3: Logout
        dashboard.logout()

        # Step 4: Verifikasi kembali ke halaman login
        assert login_page.is_login_failed() == False  # tidak ada flash error
        assert 'login' in login_page.get_current_url(), \
            'Setelah logout, user harus kembali ke halaman login'