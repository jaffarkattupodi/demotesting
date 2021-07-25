import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.add_newcustomer import Customer
from pageobjects.loginpage import login
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen
from utilities import XLutils
from selenium.webdriver.support import expected_conditions as ec
import string
import random



class Test_002_addcustomer:
    baseurl = Readconfig.getApplicationurl()
    username=Readconfig.getuseremail()
    password=Readconfig.getpassword()


    def test_addcust(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        # wait=WebDriverWait(self.driver,10)
        # alert=wait.until(ec.alert_is_present())
        # alert.accept()

        self.newcus=Customer(self.driver)
        self.newcus.clickoncustmenu()
        self.newcus.clickcustsubmenu()
        self.newcus.clickadd()
        self.email=random_generator() + "@gmail.com"
        self.newcus.setemail(self.email)
        self.newcus.setpassword('test123')
        self.newcus.setfirstname('jaffar')
        self.newcus.setlastname('vali')
        self.newcus.setgender('Male')
        self.newcus.setdob('11/2/1999')
        self.newcus.setcompanyname('wipro')
        self.newcus.rolepath('Guest')
        self.newcus.selctdrp('Vendor 1')
        self.newcus.save()

        self.msg=self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if   "The new customer has been added wsuccessfully."  in self.msg:
            assert True==True
        else:
            self.driver.save_screenshot("C:\\Users\\user\\PycharmProjects\\demotesting\\screenshots\\testaddcus.png")
            assert True==False

def random_generator(size=8, chars=string.ascii_lowercase +string.digits):
    return ''.join(random.choice(chars) for x in range(size))


