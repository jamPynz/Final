import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

class TestNaiinSearch(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

        # เปิดหน้าเว็บ naiin
        self.driver.get("https://www.naiin.com/")

        # ขยายหน้าต่างเบราว์เซอร์ให้เต็มจอ
        self.driver.maximize_window()

    def test_search_for_book(self):
        # ค้นหา element ด้วย ID
        search_box = self.driver.find_element("name", "title")

        # ส่งคีย์เวิร์ด "เขียนโปรแกรม python"
        search_box.send_keys("เขียนโปรแกรม python")

        # กด Enter
        button = self.driver.find_element("xpath", '//*[@id="header-search-from"]/div[1]/button')
        button.click()
        time.sleep(5)

        # รอให้ผลการค้นหาปรากฏขึ้น
        self.driver.implicitly_wait(10)  # รอไม่เกิน 10 วินาที

        page_content = self.driver.page_source
        self.assertIn("เขียนโปรแกรม python", page_content, "เขียนโปรแกรม python")

    def tearDown(self):
        # หยุดทำงานเป็นเวลา 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(2)

        # ปิด WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()