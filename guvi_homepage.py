import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.expected_conditions import url_matches, title_contains, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from webdriver_manager.chrome import ChromeDriverManager


class homepage():
    def __init__(self, pdriver):
        self.driver = pdriver
        self.expected_url="https://www.guvi.in/"
        self.expected_title="GUVI | Learn to code in your native language"
        self.loginbutton_locator = (By.ID, "login-btn")
        self.signupbutton_locator = (By.XPATH, "//a[text()='Sign up']")
        self.menuitem_locator = (By.XPATH, "//div[contains(@class, 'basis')]/*")
        self.dobby_locator = (By.ID, "chateleon-container-gif-0")
        self.wait = WebDriverWait(pdriver, 10)




    def validateURL(self):
         try:
             current_url=self.driver.current_url
             print(f"The current_url is {current_url}")
             assert current_url == self.expected_url,"url doesn't match"
             self.driver.save_screenshot("validateurl.png")

         except Exception as e:
             print(e)

    def validateTitle(self):
        try:
            page_title = self.driver.title
            print(f"The title is {page_title}")
            assert page_title == self.expected_title,"Expected title doesn't match"
            print("Expected title matches successfully")
            self.driver.save_screenshot("validatetitle.png")

        except Exception as e:
            print(e)

    def validate_dobby(self):
        try:
            dobby = self.wait.until(expected_conditions.visibility_of_element_located((self.dobby_locator)))
            time.sleep(10) # time.sleep is used here to get exact screenshot of dobby image since manually itself it took time to get the image in page
            assert dobby.is_displayed(), "dobby not displayed"
            print("dobby displayed successfully")
            self.driver.save_screenshot("dobbyimage.png")

        except Exception as e:
            print(e)

    def display_loginbutton(self):
        try:
            Loginbutton_displayed = self.wait.until(expected_conditions.visibility_of_element_located((self.loginbutton_locator)))
            assert Loginbutton_displayed.is_displayed(),"Login button is not displayed"
            assert Loginbutton_displayed.is_enabled(),"Login button is not enabled"
            print("Loginbutton is displayed and enabled")
            self.driver.save_screenshot("login.png")

        except Exception as e:
            print(e)

    def clickloginbutton(self):
        self.driver.find_element(*self.loginbutton_locator).click()
        current_url = self.driver.current_url
        print(current_url)
        assert current_url == "https://www.guvi.in/sign-in/","url mismatch"
        self.driver.save_screenshot("signinpage.png")

    def display_signup(self):
        try:
            signup_displayed = self.wait.until(expected_conditions.visibility_of_element_located((self.signupbutton_locator)))
            assert signup_displayed.is_displayed(),"signup button not displayed"
            assert signup_displayed.is_enabled(),"signup button not enabled"
            print("signup is displayed and enabled")
            self.driver.save_screenshot("signup.png")

        except Exception as e:
            print(e)

    def clicksignupbutton(self):
            self.driver.find_element(*self.signupbutton_locator).click()
            current_url = self.driver.current_url
            print(current_url)
            assert current_url == "https://www.guvi.in/register/","url mismatch"
            self.driver.save_screenshot("clicksignup.png")


    def validate_displaymenu(self):
        menuitems = self.driver.find_elements(*self.menuitem_locator)
        for item in menuitems[0:3]:
            if item.is_displayed() and item.is_enabled():
                print(f"Menu item displayed and enabled: {item.text}")
            else:
                print(f"Menu item not displayed or not enabled: {item.text}")
        self.driver.save_screenshot("displaymenu.png")



