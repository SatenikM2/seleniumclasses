from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MyTest():
    def prerequisite(self):
        # Prepequsites
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.youtube.com")

    def act(self):
        # act
        searchFieldElement = self.driver.find_element(By.NAME, "search_query")
        searchFieldElement.clear()
        searchFieldElement.send_keys("adele")
        searchFieldElement.send_keys(Keys.ENTER)
        musicButton = self.driver.find_element(By.XPATH,
                                               "(//div[@class='text-wrapper style-scope ytd-video-renderer'])[1]")
        musicButton.click()
        time.sleep(10)

    def Cleanup(self):
        # CleanUp
        self.driver.close()


if __name__ == "__main__":
    test = MyTest()
    test.prerequisite()
    test.act()
    test.Cleanup()

