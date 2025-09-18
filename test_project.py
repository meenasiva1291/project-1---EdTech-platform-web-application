import pytest
from project1_guviautomation.pages.guvi_homepage import homepage
from project1_guviautomation.pages.loginpage import signuppage
from project1_guviautomation.read_data_from_xl import read_data

# 1.verify whether the url https://www.guvi.in/ is valid or not
def test_testcase1_validateURL(driver):
    homepage1 = homepage(pdriver=driver)
    homepage1.validateURL()

# 2.verify whether the title of the webpage is correct
def test_testcase2_validateTitle(driver):
    validateTitle = homepage(pdriver=driver)
    validateTitle.validateTitle()

# 3.verify the visibility and clickability of the Login button
def test_testcase3_validateLoginbutton(driver):
    loginclick = homepage(pdriver=driver)
    loginclick.display_loginbutton()
    loginclick.clickloginbutton()

# 4.verify the visibility and clickability of the signup button
def test_testcase4_validatesignupbutton(driver):
    signupclick = homepage(pdriver=driver)
    signupclick.display_signup()
    signupclick.clicksignupbutton()

# 5.verify navigation to sign-in page via sign-up button
def test_testcase5_validateloginpage_via_signup(driver):
    loginpage = signuppage(driver)
    signupclick = homepage(pdriver=driver)
    signupclick.display_signup()
    loginpage.navigate_signinpage()

# 6.verify login functionality with valid credentials
@pytest.mark.parametrize("emailaddress,password", read_data())
def test_testcase6_login_validcredentials(emailaddress, password, driver):
    click_login = homepage(pdriver=driver)
    click_login.clickloginbutton()
    login_action = signuppage(driver)
    login_action.validcredentials(emailaddress, password)

#7.verify login with invalid credentials
def test_testcase7_invalidcredentials(driver):
    click_login = homepage(pdriver=driver)
    click_login.clickloginbutton()
    login_action = signuppage(driver)
    login_action.invalidcredentials()

#8.verify menu items "courses","LIVE classes","Practise" are displayed
def test_testcase8_keymenuitems(driver):
    menu = homepage(pdriver=driver)
    menu.validate_displaymenu()

#9.validate dobby guvi assistant display in homepage
def test_testcase9_validatedobby(driver):
    validatedobby = homepage(pdriver=driver)
    validatedobby.validate_dobby()

#10.validate logout functionality
@pytest.mark.parametrize("emailaddress,password", read_data())
def test_testcase10_validatelogout(emailaddress,password,driver):
    click_login = homepage(pdriver=driver)
    click_login.clickloginbutton()
    login_action = signuppage(driver)
    login_action.validcredentials(emailaddress, password)
    logout_action = signuppage(driver)
    logout_action.logout()
