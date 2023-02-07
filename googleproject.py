from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MyTest():
    def prerequisite(self):
        #Prepequsites
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com/webhp?hl=en")

    def act(self):
    #act
        searchFieldElement = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
        searchFieldElement.clear()
        searchFieldElement.send_keys("suzuki")
        searchFieldElement.send_keys(Keys.ENTER)
        time.sleep(1)
        imageButton = self.driver.find_element(By.LINK_TEXT, "Images")
        imageButton.click()
        time.sleep(1)
        firstImage = self.driver.find_element(By.XPATH, "(//a[@class='wXeWr islib nfEiy'])[1]")
        firstImage.click()
        time.sleep(2)

        #Assertion
        try:
            verification = self.driver.find_element(By.XPATH, "//img[@class='n3VNCb KAlRDb']")
        except Exception as e:
            print("Error: Image not opened")
            exit(5)
    def Cleanup(self):
    #CleanUp
        self.driver.close()

if  __name__ == "__main__":
    test = MyTest()
    test.prerequisite()
    test.act()
    test.Cleanup()



