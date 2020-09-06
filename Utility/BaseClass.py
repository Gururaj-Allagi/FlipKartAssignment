import pytest
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("setup")
class BaseClass:

    def fn_explicitWait(self, element):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element)))

    def fn_openExcel(self):
        book = Workbook()
        sheet = book.active
        # return sheet