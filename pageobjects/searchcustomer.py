class search_existing_customer:
    txt_email_id="SearchEmail"
    txt_first_id="SearchFirstName"
    txt_lastname_id="SearchLastName"
    link_search_id="search-customers"
    table_xpath="//div[@class='card card-default']"
    tablerow_xpath="//*[@id='customers-grid']/tbody/tr"
    table_column_xpath='//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self,driver):
        self.driver=driver

    def getemail(self,email):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)
    def getfirstname(self,fstname):
        self.driver.find_element_by_id(self.txt_first_id).send_keys(fstname)
    def getlastname(self,lstname):
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lstname)
    def getsearch(self):
        self.driver.find_element_by_id(self.link_search_id).click()
    def gettablerow(self):
        return len(self.driver.find_elements_by_xpath(self.tablerow_xpath))
    def gettablecolumn(self):
        return len(self.driver.find_elements_by_xpath(self.table_column_xpath))
    def searchcustomerbyemail(self,email):
        flag=False
        for r in range(1,self.gettablerow()+1):
            table=self.driver.find_element_by_id(self.table_xpath)
            emailid=table.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[2]').text
            if emailid=='email':
                flag=True
                break
            else:
                return flag

