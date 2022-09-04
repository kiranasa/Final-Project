import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class testLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        def test_Login(self):
         # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

        response_message = driver.find_element(By.ID,"menu_admin_viewAdminModule").text
        self.assertEqual(response_message, 'Admin')

        def test_Job(self):
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        driver.find_element(By.ID,"menu_admin_Job").click()
        driver.find_element(By.ID,"menu_admin_viewJobTitleList").click()
        time.sleep(3)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
        driver.find_element(By.ID,"jobTitle_jobTitle").send_keys("Staff")
        driver.find_element(By.ID,"jobTitle_jobDescription").send_keys("job description")
        driver.find_element(By.ID,"jobTitle_jobNote").send_keys("job note")
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)

        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        driver.find_element(By.ID,"menu_admin_nationality")
        driver.find_element(By.ID,"btnSave").click()
        driver.find_element(By.ID,"nationality_name").send_keys("england")
        driver.find_element(By.ID,"btnSave").click()
        time.sleep(3)

   def test_Employee(self):
        # steps
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"menu_PIM_viewPIMModule").click()
        driver.find_element(By.ID,"menu_PIM_AddEmployee").click()
        driver.find_element(By.ID,"employee_name").send_keys("Samira")
        time.sleep(3)
        driver.find_element(By.ID,"btnAdd").click()
        time.sleep(3)
    


unittest.main()


