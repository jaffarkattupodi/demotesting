import time

import pytest
from selenium import webdriver
from pageobjects.loginpage import login
from utilities.readProperties import Readconfig
from utilities.customlogger import LogGen
from utilities import XLutils
class Test_002_DDT_login:
    baseurl=Readconfig.getApplicationurl()
    # useremail=Readconfig.getuseremail()
    # password=Readconfig.getpassword()
    path='C:\\Users\\user\\Documents\\Book65.xlsx'
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info('*******Test_001_login*********')
        self.logger.info('*******verifying home page*********')

        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.rows=XLutils.getrow(self.path,'Sheet1')
        print('Number of rows:',self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=XLutils.readdata(self.path,'Sheet1',r,1)
            self.password=XLutils.readdata(self.path,'Sheet1',r,2)
            self.exp=XLutils.readdata(self.path,'Sheet1',r,3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()

            time.sleep(3)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=='pass':
                    self.logger.info("**passed")
                    self.lp.clicklogout()
                    lst_status.append('pass')
                elif self.exp=='fail':
                    self.logger.info("***fail")

                    lst_status.append('fail')
            elif act_title!=exp_title:
                if self.exp=='pass':
                    self.logger.info("**fail")

                    lst_status.append('fail')
                elif self.exp=='fail':
                    self.logger.info("**passed")

                    lst_status.append('pass')
        if 'fail' not in lst_status:
            self.logger.info('****login DDT test passed*****')
            self.driver.close()
            assert True
        else:
            self.logger.info('****login DDT test failed******')
            self.driver.close()
            assert False

        self.logger.info('******end of login DDt*****')



