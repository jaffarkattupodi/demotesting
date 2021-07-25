import time

from selenium.webdriver.support.select import Select


class Customer:
    cust_menu_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    cust_submenu_xpath="//*[text()=' Customers']"
    add_link_xpath="//a[@class='btn btn-primary']"
    user_email_id="Email"
    user_password_id="Password"
    first_name_id="FirstName"
    last_name_id="LastName"
    gender_male_id="Gender_Male"
    gender_female_id="Gender_Female"
    dob_id="DateOfBirth"
    company_name_id="Company"

    cutomer_role_xpath='//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    customer_admin_xpath="//li[text()='Administrators']"
    customer_guest_xpath="//li[text()='Guests']"
    customer_register_xpath="//li[text()='Registered']"
    customer_vendors_xpath="//li[text()='Vendors']"
    drp_id="VendorId"
    save_xpath="//button[@class='btn btn-primary'][1]"


    def __init__(self,driver):
        self.driver=driver

    def clickoncustmenu(self):
        self.driver.find_element_by_xpath(self.cust_menu_xpath).click()
    def clickcustsubmenu(self):
        self.driver.find_element_by_xpath(self.cust_submenu_xpath).click()
    def clickadd(self):
        self.driver.find_element_by_xpath(self.add_link_xpath).click()
    def setemail(self,email):
        self.driver.find_element_by_id(self.user_email_id).send_keys(email)
    def setpassword(self,password):
        self.driver.find_element_by_id(self.user_password_id).send_keys(password)
    def setfirstname(self,first):
        self.driver.find_element_by_id(self.first_name_id).send_keys(first)
    def setlastname(self,last):
        self.driver.find_element_by_id(self.last_name_id).send_keys(last)
    def setgender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.gender_male_id).click()
        else:
            self.driver.find_element_by_id(self.gender_female_id).click()
    def setdob(self,dob):
        self.driver.find_element_by_id(self.dob_id).send_keys(dob)
    def setcompanyname(self,cmpnme):
        self.driver.find_element_by_id(self.company_name_id).send_keys(cmpnme)

    def rolepath(self,role):
        self.driver.find_element_by_xpath(self.cutomer_role_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.customer_register_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element_by_xpath(self.customer_admin_xpath)
        elif role=='Guest':
            time.sleep(3)
            self.driver.find_element_by_xpath("//span[@title='delete']").click()
            self.listitem=self.driver.find_element_by_xpath(self.customer_guest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element_by_xpath(self.customer_register_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.customer_vendors_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)
    def selctdrp(self,value):
        drp=Select(self.driver.find_element_by_id(self.drp_id))
        drp.select_by_visible_text(value)
    def save(self):
        self.driver.find_element_by_xpath(self.save_xpath).click()







