class login:
    testbox_username_id="Email"
    testbox_password_id="Password"
    button_login_xpath="//button[text()='Log in']"
    button_logout_xpath="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.testbox_username_id).clear()
        self.driver.find_element_by_id(self.testbox_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.testbox_password_id).clear()
        self.driver.find_element_by_id(self.testbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()




