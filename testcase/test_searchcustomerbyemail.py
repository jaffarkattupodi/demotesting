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
from pageobjects.searchcustomer import search_existing_customer
class Test_serachcustomerbyemail():
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getuseremail()
    password = Readconfig.getpassword()
    def test_searchcustomerbyemail(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.newcust=Customer(self.driver)
        self.newcust.clickoncustmenu()
        self.newcust.clickcustsubmenu()
        searchcust=search_existing_customer(self.driver)
        searchcust.getemail('victoria_victoria@nopCommerce.com')
        searchcust.getsearch()
        time.sleep(4)
        status=searchcust.searchcustomerbyemail('victoria_victoria@nopCommerce.com')
        assert True==status
        self.driver.close()