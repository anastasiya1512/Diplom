from selenium.webdriver.common.by import By
from Pages.main_page import MainPage


class MoviePage(MainPage):
    TITLE = (By.TAG_NAME, "h1")

    def get_title(self) -> str:
        """Получает название фильма"""
        return self.wait_for_element(*self.TITLE).text
