from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import url_to_be
from selenium.webdriver.support.wait import WebDriverWait



class signuppage():
    def __init__(self,driver):
        self.driver = driver
        self.signupbutton_locator = (By.XPATH, "//a[text()='Sign up']")
        self.loginbutton_locator = (By.XPATH,"//a[text()='Login']")
        self.email_locator = (By.ID,"email")
        self.password_locator = (By.ID,"password")
        self.loginclick_locator = (By.ID,"login-btn")
        self.errormsg_locator = (By.XPATH, "(//div[text()='Incorrect Email or Password'])[1]")
        # self.navigatelogout_locator = (By.XPATH, "(//*[contains(@class,'rounded-full')])[1]")
        self.navigatelogout_locator = (By.ID,"dropdown_title")
        self.logout_locator = (By.XPATH, "//div[text()='Sign Out']")
        self.wait = WebDriverWait(driver, 10)

    def navigate_signinpage(self):
        try:
            self.driver.find_element(*self.signupbutton_locator).click()
            self.driver.find_element(*self.loginbutton_locator).click()
            current_url = self.driver.current_url
            print(current_url)
            assert current_url == 'https://www.guvi.in/sign-in/',"URL doesn't match"
            print("Navigation to sign in page via signup is successfull")
            self.driver.save_screenshot("navigatesignin.png")

        except Exception as e:
            print(e)

    def validcredentials(self,emailaddress,password):
        try:
            self.driver.find_element(*self.email_locator).send_keys(emailaddress)
            self.driver.find_element(*self.password_locator).send_keys(password)
            self.driver.save_screenshot("validcredentials.png")
            self.driver.find_element(*self.loginclick_locator).click()
            assert url_to_be("https: // www.guvi. in / courses /?current_tab = myCourses"),"url mismatch"
            print("User logged in and redirected to the profile successfully")


        except Exception as e:
            print(e)

    def invalidcredentials(self):
            try:
                self.driver.find_element(*self.email_locator).send_keys("meenakshisivasank@gmail.com")
                self.driver.find_element(*self.password_locator).send_keys("xyzz")
                self.driver.save_screenshot("invalidcredentials.png")
                self.driver.find_element(*self.loginclick_locator).click()
                error_message = self.wait.until(expected_conditions.visibility_of_element_located((self.errormsg_locator)))
                print("Not able to login due to invalid credentials")
                actual_errormsg = error_message.text
                expected_errormsg = "Incorrect Email or Password"
                assert actual_errormsg == expected_errormsg,(f"Expected error message is {expected_errormsg} but got {actual_errormsg}")

            except Exception as e:
                print(e)

    def logout(self):
        try:
           dropdown = self.wait.until(expected_conditions.visibility_of_element_located(self.navigatelogout_locator))
           dropdown.click()

           self.driver.find_element(*self.logout_locator).click()
           print("user logged out successfully")
           self.driver.save_screenshot("logout.png")

        except Exception as e:
            print(e)






