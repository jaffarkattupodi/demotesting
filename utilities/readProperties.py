import configparser
config=configparser.RawConfigParser()
config.read("C:\\Users\\user\\PycharmProjects\\demotesting\\configurations\\config.ini")
class Readconfig:
    @staticmethod
    def getApplicationurl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getuseremail():
        username=config.get('common info','useremail')
        return username
    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password
